#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
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
            'title': get_plain_text(p.get(props['title'])),
            'rawStatus': raw_status,
            'status': normalize_status(raw_status.lower(), mapping),
            'notes': get_plain_text(p.get(props['notes'])),
            'requestedBy': get_plain_text(p.get(props['requestedBy'])),
            'createdAt': get_plain_text(p.get(props['createdAt'])),
            'materialUrl': get_plain_text(p.get(props['materialUrl'])),
        })
    return rows


def fetch_cases(limit: int = 100) -> list[dict]:
    config = load_config()
    kind = config['active']['kind']
    if kind == 'notion':
        return fetch_notion_cases(limit)
    raise SystemExit(f'unsupported CS management provider: {kind}')


def open_cases(cases: list[dict]) -> list[dict]:
    return [c for c in cases if c.get('status') != 'RESOLVED']


def cmd_list_open(args):
    cases = open_cases(fetch_cases(args.limit))
    print(json.dumps(cases, ensure_ascii=False, indent=2))


def cmd_summary(_args):
    config = load_config()
    cases = fetch_cases(100)
    opened = open_cases(cases)
    by_status: dict[str, int] = {}
    for case in opened:
        by_status[case['status']] = by_status.get(case['status'], 0) + 1
    print(json.dumps({
        'tool': config['active'],
        'openCount': len(opened),
        'openByStatus': by_status,
        'openCases': opened[:10],
    }, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('list-open')
    p.add_argument('--limit', type=int, default=100)
    p.set_defaults(func=cmd_list_open)

    p = sub.add_parser('summary')
    p.set_defaults(func=cmd_summary)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
