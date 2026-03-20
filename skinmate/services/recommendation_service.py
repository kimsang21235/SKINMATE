from __future__ import annotations

from datetime import datetime


def generate_recommendations(scores: dict, username: str) -> dict:
    skin_type = scores.get('skin_type', '알 수 없음')

    skin_type_descriptions = {
        '건성': '건성 피부는 피지가 적고 건조하여 각질이 일어나기 쉬우며, 꼼꼼한 보습이 중요합니다.',
        '지성': '지성 피부는 피지 분비가 많아 번들거리기 쉽고, 모공 관리와 유수분 밸런스를 맞추는 것이 중요합니다.',
        '중성': '중성 피부는 유수분 밸런스가 안정적이지만, 계절과 환경에 따라 가벼운 조정이 필요합니다.',
        '복합 건성': '복합 건성 피부는 U존 건조가 두드러지기 쉬워 부위별 보습 전략이 필요합니다.',
        '복합 지성': '복합 지성 피부는 T존 유분과 U존 균형을 함께 고려하는 관리가 중요합니다.'
    }
    skin_type_text = skin_type_descriptions.get(skin_type, f'{skin_type} 타입의 피부를 가지고 계시네요.')

    all_scores_korean = {
        '수분': scores.get('moisture'),
        '탄력': scores.get('elasticity'),
        '주름': scores.get('wrinkle')
    }
    top_concerns_names = [name for name, score in all_scores_korean.items() if isinstance(score, (int, float)) and score <= 45]
    concern_icon_map = {'수분': 'water-icon.png', '탄력': 'elasticity-icon.png', '주름': 'wrinkle-icon.png'}
    concerns_for_template = [{'name': name, 'icon': concern_icon_map.get(name, 'default-icon.png')} for name in top_concerns_names]

    concern_intro = ''
    if set(top_concerns_names) == {'수분', '탄력', '주름'}:
        concern_intro = '현재 전반적인 피부 컨디션이 저하되어 복합 케어가 필요합니다.'
    elif '수분' in top_concerns_names and '탄력' in top_concerns_names:
        concern_intro = '피부가 건조하고 탄력이 함께 떨어진 상태입니다.'
    elif '수분' in top_concerns_names and '주름' in top_concerns_names:
        concern_intro = '수분 부족으로 잔주름이 더 도드라져 보일 수 있습니다.'
    elif '탄력' in top_concerns_names and '주름' in top_concerns_names:
        concern_intro = '탄력 저하와 주름 고민이 함께 나타나고 있습니다.'
    elif '수분' in top_concerns_names:
        concern_intro = '피부에 수분이 부족해 건조함이 느껴집니다.'
    elif '탄력' in top_concerns_names:
        concern_intro = '피부 탄력이 떨어져 탄탄함이 부족합니다.'
    elif '주름' in top_concerns_names:
        concern_intro = '주름 관리가 필요한 상태입니다.'

    rec_map = {
        ('수분',): '히알루론산, 글리세린, 세라마이드 중심의 보습 제품을 우선 추천합니다.',
        ('탄력',): '펩타이드, 콜라겐, 아데노신 계열 제품으로 탄력 케어를 권장합니다.',
        ('주름',): '레티놀, 비타민 C, 토코페롤 계열 제품으로 안티에이징 루틴을 구성해보세요.',
    }
    product_recommendation = ''
    if len(top_concerns_names) == 1:
        product_recommendation = rec_map.get(tuple(top_concerns_names), '')
    elif top_concerns_names:
        product_recommendation = '보습·탄력·안티에이징 성분을 조합한 단계별 루틴으로 꾸준히 관리해 주세요.'

    if concern_intro:
        recommendation_text = f"{skin_type_text}<br><br>{concern_intro}<br>{product_recommendation}"
    else:
        recommendation_text = f"{skin_type_text}<br><br>{username}님의 피부는 현재 큰 문제 없이 안정적입니다. 현재 루틴을 유지하면서 계절 변화에 맞춰 보습과 자외선 차단을 이어가세요."

    return {
        'skin_type': skin_type,
        'top_concerns_names': top_concerns_names,
        'concerns_for_template': concerns_for_template,
        'recommendation_text': recommendation_text,
    }


def generate_result_summary(username: str, main_score: float, skin_type: str, top_concerns_names: list[str]) -> str:
    summary = f"{username}님, 오늘 피부 종합 점수는 {round(main_score)}점입니다.<br>"
    if top_concerns_names:
        concerns_str = "', '".join(top_concerns_names)
        summary += f"진단 결과 현재 피부는 '{skin_type}' 타입으로 판단되며, '{concerns_str}'에 대한 집중 케어가 필요합니다.<br>{username}님의 피부 고민을 해결해 줄 루틴 추천을 확인해 보세요!"
    else:
        summary += f"현재 피부는 '{skin_type}' 타입이며 특별한 고민은 크지 않습니다.<br>좋은 피부 컨디션을 유지하고 있으니 현재 루틴을 꾸준히 이어가세요."
    return summary


def get_current_season() -> str:
    month = datetime.now().month
    if month in [5, 6, 7, 8, 9]:
        return 'summer'
    if month in [12, 1, 2]:
        return 'winter'
    return 'spring_fall'
