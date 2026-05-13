#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / '.env'
STATE_PATH = ROOT / 'references' / 'notion-cs-knowledge.json'
NOTION_VERSION = '2022-06-28'


def load_env():
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            os.environ.setdefault(k, v)


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
    chunks = []
    for part in [text[i:i+1800] for i in range(0, len(text), 1800)]:
        chunks.append({'type': 'text', 'text': {'content': part}})
    return chunks


def title_prop(text: str):
    return {'title': [{'type': 'text', 'text': {'content': text}}]}


def rich_prop(text: str):
    return {'rich_text': rich_text(text)}


def select_prop(value: str | None):
    return {'select': {'name': value}} if value else {'select': None}


def multi_select_prop(values):
    return {'multi_select': [{'name': v} for v in values if v]}


def date_prop(value: str | None):
    return {'date': {'start': value}} if value else {'date': None}


def url_prop(value: str | None):
    return {'url': value or None}


def create_page(parent_page_id: str, title: str, children: list[dict] | None = None):
    return notion_request('POST', '/pages', {
        'parent': {'type': 'page_id', 'page_id': parent_page_id},
        'properties': {'title': title_prop(title)},
        'children': children or [],
    })


def create_database(parent_page_id: str, title: str, properties: dict):
    return notion_request('POST', '/databases', {
        'parent': {'type': 'page_id', 'page_id': parent_page_id},
        'title': rich_text(title),
        'properties': properties,
    })


def paragraph(text: str):
    return {'object': 'block', 'type': 'paragraph', 'paragraph': {'rich_text': rich_text(text)}}


def heading(level: int, text: str):
    key = f'heading_{level}'
    return {'object': 'block', 'type': key, key: {'rich_text': rich_text(text)}}


def bullet(text: str):
    return {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': rich_text(text)}}


def seed(parent_page_id: str):
    hub = create_page(parent_page_id, 'CS Knowledge Hub', [
        heading(1, 'CS Knowledge Hub'),
        paragraph('CS 응답용 검증 지식과 재사용 가능한 답변 카드를 이곳에서 관리한다.'),
        heading(2, '운영 순서'),
        bullet('신규 material은 먼저 CS Intake Queue에 넣는다.'),
        bullet('핵심 근거를 CS Knowledge Sources로 정리한다.'),
        bullet('고객 응답용 문장으로 다듬어 CS Answer Cards를 만든다.'),
        heading(2, '인덱스 축'),
        bullet('계정/권한'),
        bullet('결제/구독'),
        bullet('데이터 연동'),
        bullet('리포트/집계'),
        bullet('광고 운영/자동화'),
        bullet('장애/지연/정합성'),
        bullet('정책/제한사항'),
    ])

    sources = create_database(parent_page_id, 'CS Knowledge Sources', {
        'Title': {'title': {}},
        'Status': {'select': {'options': [{'name': x} for x in ['inbox', 'reviewing', 'distilled', 'blocked']]}},
        'Source Type': {'select': {'options': [{'name': x} for x in ['MR', 'issue', 'doc', 'slack', 'notion', 'runbook', 'policy']]}},
        'Product Area': {'multi_select': {'options': []}},
        'Feature / Module': {'multi_select': {'options': []}},
        'Customer Impact': {'multi_select': {'options': []}},
        'Keywords': {'multi_select': {'options': []}},
        'Source URL': {'url': {}},
        'Confidence': {'select': {'options': [{'name': x} for x in ['high', 'medium', 'low']]}},
        'Last Reviewed': {'date': {}},
        'Owner': {'rich_text': {}},
        'Summary': {'rich_text': {}},
        'CS Notes': {'rich_text': {}},
    })

    cards = create_database(parent_page_id, 'CS Answer Cards', {
        'Title': {'title': {}},
        'Status': {'select': {'options': [{'name': x} for x in ['draft', 'ready', 'needs-review']]}},
        'Topic': {'multi_select': {'options': []}},
        'Audience': {'select': {'options': [{'name': x} for x in ['customer', 'internal-cs', 'both']]}},
        'Keywords': {'multi_select': {'options': []}},
        'Source Links': {'rich_text': {}},
        'Last Updated': {'date': {}},
        'Answer TL;DR': {'rich_text': {}},
        'When to Use': {'rich_text': {}},
        'Do Not Say': {'rich_text': {}},
        'Escalate If': {'rich_text': {}},
    })

    intake = create_database(parent_page_id, 'CS Intake Queue', {
        'Title': {'title': {}},
        'Status': {'select': {'options': [{'name': x} for x in ['new', 'processing', 'blocked', 'done']]}},
        'Material URL': {'url': {}},
        'Material Type': {'select': {'options': [{'name': x} for x in ['MR', 'issue', 'doc', 'message', 'policy', 'other']]}},
        'Requested By': {'rich_text': {}},
        'Notes': {'rich_text': {}},
        'Created At': {'date': {}},
    })

    state = {
        'parent_page_id': parent_page_id,
        'hub_page_id': hub['id'],
        'sources_db_id': sources['id'],
        'answer_cards_db_id': cards['id'],
        'intake_db_id': intake['id'],
    }
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2))
    print(json.dumps(state, ensure_ascii=False, indent=2))


def load_state():
    if not STATE_PATH.exists():
        raise SystemExit(f'state file missing: {STATE_PATH}')
    return json.loads(STATE_PATH.read_text())


def create_db_page(database_id: str, properties: dict, children: list[dict] | None = None):
    payload = {
        'parent': {'database_id': database_id},
        'properties': properties,
    }
    if children:
        payload['children'] = children
    return notion_request('POST', '/pages', payload)


def add_intake(title: str, url: str, requested_by: str, notes: str, material_type: str, status: str):
    state = load_state()
    page = create_db_page(state['intake_db_id'], {
        'Title': title_prop(title),
        'Status': select_prop(status),
        'Material URL': url_prop(url),
        'Material Type': select_prop(material_type),
        'Requested By': rich_prop(requested_by),
        'Notes': rich_prop(notes),
        'Created At': date_prop(str(date.today())),
    })
    print(json.dumps({'id': page['id'], 'url': page['url']}, ensure_ascii=False, indent=2))


def add_source(title: str, url: str, summary: str, notes: str, source_type: str, status: str, confidence: str, keywords: list[str], product_areas: list[str], modules: list[str]):
    state = load_state()
    page = create_db_page(state['sources_db_id'], {
        'Title': title_prop(title),
        'Status': select_prop(status),
        'Source Type': select_prop(source_type),
        'Product Area': multi_select_prop(product_areas),
        'Feature / Module': multi_select_prop(modules),
        'Keywords': multi_select_prop(keywords),
        'Source URL': url_prop(url),
        'Confidence': select_prop(confidence),
        'Last Reviewed': date_prop(str(date.today())),
        'Summary': rich_prop(summary),
        'CS Notes': rich_prop(notes),
    })
    print(json.dumps({'id': page['id'], 'url': page['url']}, ensure_ascii=False, indent=2))


def add_card(title: str, answer: str, when_to_use: str, do_not_say: str, escalate_if: str, status: str, audience: str, keywords: list[str], topics: list[str], source_links: str):
    state = load_state()
    page = create_db_page(state['answer_cards_db_id'], {
        'Title': title_prop(title),
        'Status': select_prop(status),
        'Topic': multi_select_prop(topics),
        'Audience': select_prop(audience),
        'Keywords': multi_select_prop(keywords),
        'Source Links': rich_prop(source_links),
        'Last Updated': date_prop(str(date.today())),
        'Answer TL;DR': rich_prop(answer),
        'When to Use': rich_prop(when_to_use),
        'Do Not Say': rich_prop(do_not_say),
        'Escalate If': rich_prop(escalate_if),
    })
    print(json.dumps({'id': page['id'], 'url': page['url']}, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('seed')
    p.add_argument('--page-id', required=True)

    p = sub.add_parser('add-intake')
    p.add_argument('--title', required=True)
    p.add_argument('--url', required=True)
    p.add_argument('--requested-by', default='')
    p.add_argument('--notes', default='')
    p.add_argument('--material-type', default='other')
    p.add_argument('--status', default='new')

    p = sub.add_parser('add-source')
    p.add_argument('--title', required=True)
    p.add_argument('--url', required=True)
    p.add_argument('--summary', default='')
    p.add_argument('--notes', default='')
    p.add_argument('--source-type', default='doc')
    p.add_argument('--status', default='reviewing')
    p.add_argument('--confidence', default='medium')
    p.add_argument('--keywords', default='')
    p.add_argument('--product-areas', default='')
    p.add_argument('--modules', default='')

    p = sub.add_parser('add-card')
    p.add_argument('--title', required=True)
    p.add_argument('--answer', default='')
    p.add_argument('--when-to-use', default='')
    p.add_argument('--do-not-say', default='')
    p.add_argument('--escalate-if', default='')
    p.add_argument('--status', default='draft')
    p.add_argument('--audience', default='both')
    p.add_argument('--keywords', default='')
    p.add_argument('--topics', default='')
    p.add_argument('--source-links', default='')

    args = parser.parse_args()
    if args.cmd == 'seed':
        seed(args.page_id)
    elif args.cmd == 'add-intake':
        add_intake(args.title, args.url, args.requested_by, args.notes, args.material_type, args.status)
    elif args.cmd == 'add-source':
        add_source(
            args.title, args.url, args.summary, args.notes, args.source_type, args.status, args.confidence,
            [x.strip() for x in args.keywords.split(',') if x.strip()],
            [x.strip() for x in args.product_areas.split(',') if x.strip()],
            [x.strip() for x in args.modules.split(',') if x.strip()],
        )
    elif args.cmd == 'add-card':
        add_card(
            args.title, args.answer, args.when_to_use, args.do_not_say, args.escalate_if,
            args.status, args.audience,
            [x.strip() for x in args.keywords.split(',') if x.strip()],
            [x.strip() for x in args.topics.split(',') if x.strip()],
            args.source_links,
        )

if __name__ == '__main__':
    main()
