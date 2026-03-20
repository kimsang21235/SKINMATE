from __future__ import annotations

import json


def fromjson(json_string):
    if json_string is None:
        return {}
    try:
        return json.loads(json_string)
    except Exception:
        return {}


def get_face_icon_for_score(score):
    if score is None:
        return 'face3.png'
    score = float(score)
    if 0 <= score <= 19:
        return 'face5.png'
    if 20 <= score <= 49:
        return 'face4.png'
    if 50 <= score <= 60:
        return 'face3.png'
    if 61 <= score <= 90:
        return 'face2.png'
    return 'face1.png'
