from __future__ import annotations

import importlib.util
from pathlib import Path
from flask import current_app

from skinmate.db import get_db
from skinmate.services.recommendation_service import get_current_season

_RULES = None


def _load_rules():
    global _RULES
    if _RULES is not None:
        return _RULES
    rules_path = Path(current_app.root_path) / 'resources' / 'routine_rules.py'
    spec = importlib.util.spec_from_file_location('skinmate_routine_rules', rules_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _RULES = module.ROUTINE_RULES
    return _RULES


def build_query_from_rule(rule_query: dict):
    base_query = 'SELECT * FROM products WHERE 1=1'
    params = []
    if 'main_category' in rule_query:
        base_query += ' AND main_category = ?'
        params.append(rule_query['main_category'])
    if rule_query.get('middle_category_in'):
        placeholders = ','.join('?' for _ in rule_query['middle_category_in'])
        base_query += f' AND middle_category IN ({placeholders})'
        params.extend(rule_query['middle_category_in'])
    if rule_query.get('sub_category_in'):
        placeholders = ','.join('?' for _ in rule_query['sub_category_in'])
        base_query += f' AND sub_category IN ({placeholders})'
        params.extend(rule_query['sub_category_in'])
    if rule_query.get('positive_keywords'):
        likes = ' OR '.join(['name LIKE ?'] * len(rule_query['positive_keywords']))
        base_query += f' AND ({likes})'
        params.extend([f"%{kw}%" for kw in rule_query['positive_keywords']])
    if rule_query.get('negative_keywords'):
        not_likes = ' AND '.join(['name NOT LIKE ?'] * len(rule_query['negative_keywords']))
        base_query += f' AND ({not_likes})'
        params.extend([f"%{kw}%" for kw in rule_query['negative_keywords']])
    base_query += ' ORDER BY rank ASC LIMIT 3'
    return base_query, params


def get_products_by_query(query: str, params=()):
    db = get_db()
    products = db.execute(query, params).fetchall()
    if not products:
        return None, []
    primary = dict(products[0])
    alternatives = [dict(p) for p in products[1:3]]
    return primary, alternatives


def get_routine_from_rules(routine_type: str, skin_type: str, concerns: list[dict], current_season: str | None = None):
    current_season = current_season or get_current_season()
    rules = _load_rules()
    steps = []
    user_concerns = {c.get('name') for c in concerns if c.get('name')}

    if '주름' in user_concerns or '탄력' in user_concerns:
        concern_key = 'wrinkle_elasticity'
    elif '수분' in user_concerns:
        concern_key = 'moisture'
    else:
        concern_key = 'default'

    season_rules = rules.get(routine_type, {}).get(current_season, {})
    concern_rules = season_rules.get(concern_key, season_rules.get('default', {}))
    skin_type_rules = concern_rules.get(skin_type, concern_rules.get('Normal', []))

    for rule in skin_type_rules:
        query, params = build_query_from_rule(rule['query'])
        primary, alternatives = get_products_by_query(query, params)
        steps.append({
            'step_title': rule['title'],
            'step_description': rule['desc'],
            'primary_recommendation': primary,
            'alternatives': alternatives,
        })
    return steps



def build_recommendations_payload(username: str, skin_type: str, concerns: list[dict], makeup: str = 'no') -> dict:
    current_season = get_current_season()
    morning_routine = get_routine_from_rules('morning', skin_type, concerns, current_season)
    night_routine = get_routine_from_rules('night', skin_type, concerns, current_season)
    from datetime import datetime
    now = datetime.now()
    user_info = {
        'username': username,
        'date_info': {'year': now.year, 'month': now.month, 'day': now.day},
        'skin_type': skin_type,
        'concerns': concerns,
        'season': current_season,
        'makeup': makeup,
    }
    return {
        'user_info': user_info,
        'morning_routine': morning_routine,
        'night_routine': night_routine,
    }
