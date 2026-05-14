#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / '.env'
CONFIG_PATH = ROOT / 'state' / 'cs-management-tool.json'
NOTION_VERSION = '2022-06-28'


def load_env():
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            os.environ.setdefault(k, v)


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise SystemExit(f'missing config: {CONFIG_PATH}')
    return json.loads(CONFIG_PATH.read_text())


def notion_request(method: str, path: str, payload: dict | None = None):
    load_env()
    key = os.environ.get('NOTION_API_KEY')
    if not key:
        raise SystemExit('NOTION_API_KEY missing')
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode()
    req = urllib.request.Request(
        f'https://api.notion.com/v1{path}',
        data=data,
        method=method,
        headers={
            'Authorization': f'Bearer {key}',
            'Notion-Version': NOTION_VERSION,
            'Content-Type': 'application/json',
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors='replace')
        raise SystemExit(f'Notion API error {e.code}: {body}')


def rich_text(text: str):
    if not text:
        return []
    return [
        {'type': 'text', 'text': {'content': part}}
        for part in [text[i:i+1800] for i in range(0, len(text), 1800)]
    ]


def rich_prop(text: str):
    return {'rich_text': rich_text(text)}


def select_prop(value: str | None):
    return {'select': {'name': value}} if value else {'select': None}


def notion_update_page(page_id: str, properties: dict):
    return notion_request('PATCH', f'/pages/{page_id}', {'properties': properties})


def iso_now() -> str:
    return datetime.now().astimezone().isoformat(timespec='seconds')


def get_plain_text(prop: dict | None) -> str:
    if not prop:
        return ''
    ptype = prop.get('type')
    if ptype == 'title':
        return ''.join(x.get('plain_text', '') for x in prop.get('title', []))
    if ptype == 'rich_text':
        return ''.join(x.get('plain_text', '') for x in prop.get('rich_text', []))
    if ptype == 'select':
        sel = prop.get('select') or {}
        return sel.get('name', '')
    if ptype == 'url':
        return prop.get('url') or ''
    if ptype == 'date':
        date = prop.get('date') or {}
        return date.get('start', '')
    return ''


def normalize_status(raw_status: str, mapping: dict[str, str]) -> str:
    key = (raw_status or '').strip()
    if not key:
        return 'NEW'
    mapped = mapping.get(key)
    if mapped:
        return mapped
    upper = key.upper()
    return upper if upper in {'NEW', 'TRIAGED', 'ASSIGNED', 'PENDING', 'RESOLVED'} else key


def fetch_notion_cases(limit: int = 100) -> list[dict]:
    config = load_config()
    notion = config['providers']['notion']
    props = notion['properties']
    mapping = notion.get('statusMapping', {})
    payload = {
        'page_size': limit,
        'sorts': [
            {
                'property': props['createdAt'],
                'direction': 'descending'
            }
        ]
    }
    result = notion_request('POST', f"/databases/{notion['databaseId']}/query", payload)
    rows = []
    for item in result.get('results', []):
        p = item.get('properties', {})
        raw_status = get_plain_text(p.get(props['status']))
        rows.append({
            'id': item.get('id'),
            'url': item.get('url', ''),
            'csNo': get_plain_text(p.get(props.get('csNo'))) if props.get('csNo') else '',
            'title': get_plain_text(p.get(props['title'])),
            'rawStatus': raw_status,
            'status': normalize_status(raw_status.lower(), mapping),
            'notes': get_plain_text(p.get(props['notes'])),
            'requestedBy': get_plain_text(p.get(props['requestedBy'])),
            'createdAt': get_plain_text(p.get(props['createdAt'])),
            'resolvedAt': get_plain_text(p.get(props.get('resolvedAt'))) if props.get('resolvedAt') else '',
            'materialUrl': get_plain_text(p.get(props['materialUrl'])),
        })
    return rows


def sync_resolved_timestamps(limit: int = 200) -> dict:
    config = load_config()
    notion = config['providers']['notion']
    props = notion['properties']
    resolved_prop = props.get('resolvedAt')
    if config['active']['kind'] != 'notion' or not resolved_prop:
        return {'updated': 0, 'resolvedSet': 0, 'resolvedCleared': 0}

    cases = fetch_notion_cases(limit)
    updated = 0
    resolved_set = 0
    resolved_cleared = 0
    for case in cases:
        want_value = case['status'] == 'RESOLVED'
        has_value = bool(case.get('resolvedAt'))
        if want_value and not has_value:
            notion_update_page(case['id'], {resolved_prop: {'date': {'start': iso_now()}}})
            updated += 1
            resolved_set += 1
        elif not want_value and has_value:
            notion_update_page(case['id'], {resolved_prop: {'date': None}})
            updated += 1
            resolved_cleared += 1
    return {'updated': updated, 'resolvedSet': resolved_set, 'resolvedCleared': resolved_cleared}


def fetch_cases(limit: int = 100, syncResolvedAt: bool = True) -> list[dict]:
    config = load_config()
    kind = config['active']['kind']
    if kind == 'notion':
        if syncResolvedAt:
            sync_resolved_timestamps(max(limit, 200))
        return fetch_notion_cases(limit)
    raise SystemExit(f'unsupported CS management provider: {kind}')


def open_cases(cases: list[dict]) -> list[dict]:
    return [c for c in cases if c.get('status') != 'RESOLVED']


def append_note(existing: str, addition: str) -> str:
    existing = (existing or '').strip()
    addition = (addition or '').strip()
    if not existing:
        return addition
    if not addition:
        return existing
    return f'{existing}\n\n{addition}'


def update_case_status(case_id: str, status: str):
    config = load_config()
    notion = config['providers']['notion']
    props = notion['properties']
    if config['active']['kind'] != 'notion':
        raise SystemExit('unsupported CS management provider for update-status')
    properties = {props['status']: select_prop(status)}
    resolved_prop = props.get('resolvedAt')
    if resolved_prop:
        properties[resolved_prop] = {'date': {'start': iso_now()}} if status == 'RESOLVED' else {'date': None}
    return notion_update_page(case_id, properties)


def add_answer_record(case_id: str, answer_note: str, next_status: str | None = None):
    config = load_config()
    notion = config['providers']['notion']
    props = notion['properties']
    cases = fetch_cases(200)
    target = next((c for c in cases if c['id'] == case_id), None)
    if not target:
        raise SystemExit(f'case not found: {case_id}')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    record = f'[Answer Record {timestamp}] {answer_note}'
    merged_notes = append_note(target.get('notes', ''), record)
    properties = {props['notes']: rich_prop(merged_notes)}
    if next_status:
        properties[props['status']] = select_prop(next_status)
        resolved_prop = props.get('resolvedAt')
        if resolved_prop:
            properties[resolved_prop] = {'date': {'start': iso_now()}} if next_status == 'RESOLVED' else {'date': None}
    return notion_update_page(case_id, properties)


def cmd_list_open(args):
    cases = open_cases(fetch_cases(args.limit))
    print(json.dumps(cases, ensure_ascii=False, indent=2))


def cmd_summary(_args):
    config = load_config()
    sync_result = sync_resolved_timestamps(200)
    cases = fetch_cases(100, syncResolvedAt=False)
    opened = open_cases(cases)
    by_status: dict[str, int] = {}
    for case in opened:
        by_status[case['status']] = by_status.get(case['status'], 0) + 1
    print(json.dumps({
        'tool': config['active'],
        'resolvedAtSync': sync_result,
        'openCount': len(opened),
        'openByStatus': by_status,
        'openCases': opened[:10],
    }, ensure_ascii=False, indent=2))


def cmd_update_status(args):
    update_case_status(args.case_id, args.status)
    print(json.dumps({'ok': True, 'caseId': args.case_id, 'status': args.status}, ensure_ascii=False, indent=2))


def cmd_add_answer_record(args):
    add_answer_record(args.case_id, args.note, args.status)
    print(json.dumps({'ok': True, 'caseId': args.case_id, 'status': args.status or None}, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('list-open')
    p.add_argument('--limit', type=int, default=100)
    p.set_defaults(func=cmd_list_open)

    p = sub.add_parser('summary')
    p.set_defaults(func=cmd_summary)

    p = sub.add_parser('sync-resolved-at')
    p.add_argument('--limit', type=int, default=200)
    p.set_defaults(func=lambda args: print(json.dumps(sync_resolved_timestamps(args.limit), ensure_ascii=False, indent=2)))

    p = sub.add_parser('update-status')
    p.add_argument('--case-id', required=True)
    p.add_argument('--status', required=True, choices=['NEW', 'TRIAGED', 'ASSIGNED', 'PENDING', 'RESOLVED'])
    p.set_defaults(func=cmd_update_status)

    p = sub.add_parser('add-answer-record')
    p.add_argument('--case-id', required=True)
    p.add_argument('--note', required=True)
    p.add_argument('--status', choices=['NEW', 'TRIAGED', 'ASSIGNED', 'PENDING', 'RESOLVED'])
    p.set_defaults(func=cmd_add_answer_record)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
