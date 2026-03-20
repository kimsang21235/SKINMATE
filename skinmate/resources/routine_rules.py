ROUTINE_RULES = {
        'morning': {
            'summer': {   # ... 여름 규칙 정의
                'wrinkle_elasticity': {
                    'Dry': [   # 여름, 주름/탄력, 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['밀크', '로션', '젤', '워터'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Oily': [ # 여름, 주름/탄력, 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '밤사이 쌓인 노폐물을 씻어내요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','모공'],
                                    'positive_keywords': ['워터', '젤', '폼','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '다시 수분으로 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','모공'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드','그린','녹차','티트리','병풀'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '안티에이징으로 탄력있는 하루를 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','수분크림','수분 크림'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Normal': [ # 여름, 주름/탄력, 중성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '가벼운 물세안/순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['약산성', '세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '피부결을 따라 수분을 흡수시켜요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['펩타이드','어성초','병풀'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'CombinationDry': [ # 여름, 주름/탄력, 복합 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부에 자극이 되지 않도록 순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '끈적임 없이 가볍게 흡수되는 안티에이징.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '유분이 많은 T존은 가볍게, 건조한 U존은 얇게 덧발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'CombinationOily': [ # 여름, 주름/탄력, 복합 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                },
                'moisture' : { 
                    'Dry': [   # 여름, 수분, 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '물세안이나 가벼운 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['밀크', '로션', '젤', '워터'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '즉각적인 수분 보충으로 피부를 케어해요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['병풀','히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '수분보호막을 형성해 피부를 지켜줘요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Oily': [ # 여름, 주름/탄력, 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '밤사이 쌓인 노폐물을 씻어내요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['젤', '폼','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '다시 수분으로 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '가벼운 수분크림으로 하루를 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','수분크림','수분 크림','젤'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Normal': [ # 여름, 수분, 중성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '가벼운 물세안/순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['약산성', '세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '피부결을 따라 수분을 흡수시켜요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','병풀'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'CombinationDry': [ # 여름, 수분, 복합 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부에 자극이 되지 않도록 순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '끈적임 없이 가볍게 흡수되는 안티에이징.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '유분이 많은 T존은 가볍게, 건조한 U존은 얇게 덧발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'CombinationOily': [ # 여름, 수분, 복합 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                },
                'default': { # 특정 고민이 없을 때의 기본 규칙
                    'Dry': [ # 여름, 기본, 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','병풀','어성초'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Oily': [ # 여름, 기본, 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['수분크림','수분 크림','수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Normal': [ # 여름, 기본, 중성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['그린','녹차','병풀','어성초'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'CombinationDry': [ # 여름, 기본, 복합 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['병풀','어성초','히알루론산'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'CombinationOily': [ # 여름, 기본, 복합 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['약산성','세이프','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['그린','녹차','병풀','어성초'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['병풀','어성초','수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }]
                }
            },
            'winter': {   # ... 겨울 규칙 정의
                'wrinkle_elasticity': {
                    'Dry': [   # 겨울, 주름/탄력, 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['밀크', '로션', '젤', '워터'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','판테놀']
                                } 
                        }],
                    'Oily': [ # 겨울, 주름/탄력, 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '밤사이 쌓인 노폐물을 씻어내요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','모공'],
                                    'positive_keywords': ['워터', '젤', '폼','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '다시 수분으로 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','모공'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '안티에이징으로 탄력있는 하루를 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','수분크림','수분 크림'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Normal': [ # 겨울, 주름/탄력, 중성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '가벼운 물세안/순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '피부결을 따라 수분을 흡수시켜요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['펩타이드','어성초','병풀'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationDry': [ # 겨울, 주름/탄력, 복합 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부에 자극이 되지 않도록 순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '끈적임 없이 가볍게 흡수되는 안티에이징.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '유분이 많은 T존은 가볍게, 건조한 U존은 얇게 덧발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','판테놀']
                                } 
                        }],
                    'CombinationOily': [ # 겨울, 주름/탄력, 복합 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질'],
                                    'positive_keywords': ['약산성','그린','녹차','세이프','워터'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','오일','판테놀']
                                } 
                        }],
                },
                'moisture' : { 
                    'Dry': [   # 겨울, 수분, 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '물세안이나 가벼운 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['밀크', '로션'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '즉각적인 수분 보충으로 피부를 케어해요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['병풀','히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '수분보호막을 형성해 피부를 지켜줘요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥','판테놀']
                                } 
                        }],
                    'Oily': [ # 겨울, 수분, 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '밤사이 쌓인 노폐물을 씻어내요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['젤', '폼','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '다시 수분으로 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '안티에이징으로 탄력있는 하루를 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','수분크림','수분 크림','젤','로션'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','오일','판테놀']
                                } 
                        }],
                    'Normal': [ # 겨울, 수분, 중성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '가벼운 물세안/순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['약산성', '세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '피부결을 따라 수분을 흡수시켜요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','병풀'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationDry': [ # 겨울, 수분, 복합 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부에 자극이 되지 않도록 순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '끈적임 없이 가볍게 흡수되는 안티에이징.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산', '병풀','어성초'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '유분이 많은 T존은 가볍게, 건조한 U존은 얇게 덧발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','펩타이드'],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationOily': [ # 겨울, 수분, 복합 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['펩타이드','병풀','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                },
                'default': { # 특정 고민이 없을 때의 기본 규칙
                    'Dry': [   # 겨울, 기본, 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '물세안이나 가벼운 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['밀크', '로션'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '즉각적인 수분 보충으로 피부를 케어해요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['병풀','히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '수분보호막을 형성해 피부를 지켜줘요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥','판테놀']
                                } 
                        }],
                    'Oily': [ # 겨울, 기본, 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '밤사이 쌓인 노폐물을 씻어내요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['젤', '폼','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '다시 수분으로 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '안티에이징으로 탄력있는 하루를 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','수분크림','수분 크림','젤','로션'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','오일','판테놀']
                                } 
                        }],
                    'Normal': [ # 겨울, 기본, 중성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '가벼운 물세안/순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['약산성', '세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '피부결을 따라 수분을 흡수시켜요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','병풀'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationDry': [ # 겨울, 기본, 복합 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부에 자극이 되지 않도록 순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '끈적임 없이 가볍게 흡수되는 안티에이징.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산', '병풀','어성초'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '유분이 많은 T존은 가볍게, 건조한 U존은 얇게 덧발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','펩타이드'],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationOily': [ # 겨울, 기본, 복합 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['병풀','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                },
            },
            'spring_fall': {   # ... 환절기 규칙 정의
                'wrinkle_elasticity': {
                    'Dry': [   # 환절기, 주름/탄력, 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['밀크', '로션', '젤', '워터'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','판테놀']
                                } 
                        }],
                    'Oily': [ # 환절기, 주름/탄력, 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '밤사이 쌓인 노폐물을 씻어내요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','모공'],
                                    'positive_keywords': ['워터', '젤', '폼','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '다시 수분으로 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','모공'],
                                    'positive_keywords': ['비타민','어성초','병풀','펩타이드','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '안티에이징으로 탄력있는 하루를 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','수분크림','수분 크림'],
                                    'positive_keywords': ['어성초','병풀','펩타이드'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Normal': [ # 환절기, 주름/탄력, 중성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '가벼운 물세안/순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '피부결을 따라 수분을 흡수시켜요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','병풀'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationDry': [ # 환절기, 주름/탄력, 복합 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부에 자극이 되지 않도록 순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '끈적임 없이 가볍게 흡수되는 안티에이징.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '유분이 많은 T존은 가볍게, 건조한 U존은 얇게 덧발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','판테놀']
                                } 
                        }],
                    'CombinationOily': [ # 환절기, 주름/탄력, 복합 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질'],
                                    'positive_keywords': ['약산성','그린','녹차','세이프','워터'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','모공'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','오일','판테놀']
                                } 
                        }],
                },
                'moisture' : { 
                    'Dry': [   # 환절기, 수분, 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '물세안이나 가벼운 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['밀크', '로션'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '즉각적인 수분 보충으로 피부를 케어해요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['병풀','히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '수분보호막을 형성해 피부를 지켜줘요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','판테놀']
                                } 
                        }],
                    'Oily': [ #환절기, 수분, 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '밤사이 쌓인 노폐물을 씻어내요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['젤', '폼','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '다시 수분으로 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '안티에이징으로 탄력있는 하루를 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','수분크림','수분 크림','젤','로션'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','오일','판테놀']
                                } 
                        }],
                    'Normal': [ # 환절기, 수분, 중성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '가벼운 물세안/순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['약산성', '세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '피부결을 따라 수분을 흡수시켜요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','병풀'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationDry': [ # 환절기, 수분, 복합 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부에 자극이 되지 않도록 순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '끈적임 없이 가볍게 흡수되는 안티에이징.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산', '병풀','어성초'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '유분이 많은 T존은 가볍게, 건조한 U존은 얇게 덧발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationOily': [ # 환절기, 수분, 복합 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['병풀','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                },
                'default': { # 특정 고민이 없을 때의 기본 규칙
                    'Dry': [   # 환절기, 기본, 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '물세안이나 가벼운 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['밀크', '로션'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '즉각적인 수분 보충으로 피부를 케어해요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['병풀','히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '수분보호막을 형성해 피부를 지켜줘요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','판테놀']
                                } 
                        }],
                    'Oily': [ # 환절기, 기본, 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '밤사이 쌓인 노폐물을 씻어내요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['젤', '폼','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '다시 수분으로 채워줘요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','모공'],
                                    'positive_keywords': ['그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '안티에이징으로 탄력있는 하루를 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','수분크림','수분 크림','젤','로션'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','오일','판테놀']
                                } 
                        }],
                    'Normal': [ # 환절기, 기본, 중성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '가벼운 물세안/순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['약산성', '세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '피부결을 따라 수분을 흡수시켜요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','병풀'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationDry': [ # 환절기, 기본, 복합 건성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '피부에 자극이 되지 않도록 순한 클렌저를 사용해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '끈적임 없이 가볍게 흡수되는 안티에이징.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['히알루론산', '병풀','어성초'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '유분이 많은 T존은 가볍게, 건조한 U존은 얇게 덧발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                    'CombinationOily': [ # 환절기, 기본, 복합 지성
                        {'title': 'STEP 1. 아침 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 스킨 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','모공'],
                                    'positive_keywords': ['병풀','그린','녹차'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['딥','리치','판테놀']
                                } 
                        }],
                },
            },
        },   # ------------------------------- 나이트 루틴 -----------------------------------
        'night': {
            'summer': {   # ... 여름 규칙 정의
                'wrinkle_elasticity': {
                    'Dry': [   # 여름, 주름/탄력, 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['오일','밤','팩폼'],
                                    'negative_keywords': ['딥']
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': []
                                } 
                        }],
                    'Oily': [ # 여름, 주름/탄력, 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['오일','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': ['딥','고보습','오일']
                                } 
                        }],
                    'Normal': [ # 여름, 주름/탄력, 중성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['오일','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['어성초','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationDry': [ # 여름, 주름/탄력, 복합 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['오일','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationOily': [ # 여름, 주름/탄력, 복합 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['오일','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['촉촉', '수분','비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': ['딥','고보습','오일']
                                } 
                        }],
                },
                'moisture' : { 
                    'Dry': [   # 여름, 수분, 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['오일','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': []
                                } 
                        }],
                    'Oily': [ # 여름, 주름/탄력, 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['오일','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['촉촉', '수분','비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': ['딥','고보습','오일']
                                } 
                        }],
                    'Normal': [ # 여름, 수분, 중성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['오일','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산','병풀','어성초','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationDry': [ # 여름, 수분, 복합 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['오일','밤','팩폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산','비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분','비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': ['오일','리치']
                                } 
                        }],
                    'CombinationOily': [ # 여름, 수분, 복합 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '피부 장벽을 지켜요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['오일','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분을 채워줘요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드'],
                                    'negative_keywords': ['딥','오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '산뜻한 안티에이징으로 아침을 시작해요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습'],
                                    'positive_keywords': ['비타민','아데노신','나이아신','펩타이드','고보습','딥'],
                                    'negative_keywords': ['딥','고보습','오일']
                                } 
                        }],
                },
                'default': { # 특정 고민이 없을 때의 기본 규칙
                    'Dry': [ # 여름, 기본, 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너','에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','병풀','어성초'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산', '촉촉', '수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Oily': [ # 여름, 기본, 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['약산성'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['수분크림','수분 크림','수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'Normal': [ # 여름, 기본, 중성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['약산성','세이프'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['그린','녹차','병풀','어성초','히알루론산'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'CombinationDry': [ # 여름, 기본, 복합 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['밤','오일'],
                                    'negative_keywords': ['리치']
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['스킨/토너'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['병풀','어성초','히알루론산'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','펩타이드','어성초','수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }],
                    'CombinationOily': [ # 여름, 기본, 복합 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['약산성','세이프','그린','녹차','티트리'],
                                    'negative_keywords': ['딥','오일','팩','리치']
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['그린','녹차','병풀','어성초','히알루론산'],
                                    'negative_keywords': ['딥','오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','병풀','어성초','수분'],
                                    'negative_keywords': ['딥','리치','오일','판테놀','고보습']
                                } 
                        }]
                }
            },
            'winter': {   # ... 겨울 규칙 정의
                'wrinkle_elasticity': {
                    'Dry': [   # 겨울, 주름/탄력, 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['밀크','워터','젤','로션','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','병풀','어성초','수분'],
                                    'negative_keywords': []
                                } 
                        }],
                    'Oily': [ # 겨울, 주름/탄력, 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','팩폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','병풀','어성초','수분'],
                                    'negative_keywords': ['오일','리치']
                                } 
                        }],
                    'Normal': [ # 겨울, 주름/탄력, 중성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민'],
                                    'negative_keywords': ['오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationDry': [ # 겨울, 주름/탄력, 복합 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','밀크'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민'],
                                    'negative_keywords': ['오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationOily': [ # 겨울, 주름/탄력, 복합 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민'],
                                    'negative_keywords': ['오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['오일']
                                } 
                        }],
                },
                'moisture' : { 
                    'Dry': [   # 겨울, 수분, 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'Oily': [ # 겨울, 수분, 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','팩폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': ['오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['오일','딥','리치']
                                } 
                        }],
                    'Normal': [ # 겨울, 수분, 중성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationDry': [ # 겨울, 수분, 복합 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','밀크'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','히알루론산','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationOily': [ # 겨울, 수분, 복합 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['로션','크림'],
                                    'negative_keywords': ['오일','딥']
                                } 
                        }],
                },
                'default': { # 특정 고민이 없을 때의 기본 규칙
                    'Dry': [   # 겨울, 기본, 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'Oily': [ # 겨울, 기본, 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','팩폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': ['오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['오일','딥','리치']
                                } 
                        }],
                    'Normal': [ # 겨울, 기본, 중성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationDry': [ # 겨울, 기본, 복합 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','밀크'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','히알루론산','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationOily': [ # 겨울, 기본, 복합 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['로션','크림'],
                                    'negative_keywords': ['오일','딥']
                                } 
                        }],
                },
            },
            'spring_fall': {   # ... 환절기 규칙 정의
                'wrinkle_elasticity': {
                    'Dry': [   # 환절기, 주름/탄력, 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질'],
                                    'positive_keywords': ['밀크','워터','젤','로션','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        }],
                    'Oily': [ # 환절기, 주름/탄력, 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질'],
                                    'positive_keywords': ['오일','밤','팩폼','딥'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','병풀','어성초'],
                                    'negative_keywords': ['오일','밤','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['오일']
                                } 
                        }],
                    'Normal': [ # 환절기, 주름/탄력, 중성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질'],
                                    'positive_keywords': ['오일','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질','모공'],
                                    'positive_keywords': ['병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationDry': [ # 환절기, 주름/탄력, 복합 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질'],
                                    'positive_keywords': ['밀크','워터','젤','로션','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습'],
                                    'positive_keywords': ['판테놀','히알루론산','펩타이드','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질','모공'],
                                    'positive_keywords': ['히알루론산','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationOily': [ # 환절기, 주름/탄력, 복합 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질'],
                                    'positive_keywords': ['밀크','워터','젤','로션','클렌저','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','병풀','어성초'],
                                    'negative_keywords': ['오일']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['안티에이징','리페어','수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['오일','딥','리치']
                                } 
                        }],
                },
                'moisture' : { 
                    'Dry': [   # 환절기, 수분, 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['밀크','로션','젤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'Oily': [ # 환절기, 수분, 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','팩폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': ['오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['오일','딥','리치']
                                } 
                        }],
                    'Normal': [ # 환절기, 수분, 중성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationDry': [ # 환절기, 수분, 복합 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['밤','밀크'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','히알루론산','펩타이드','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationOily': [ # 겨울, 수분, 복합 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','딥'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['로션','크림'],
                                    'negative_keywords': ['오일','딥']
                                } 
                        }],
                },
                'default': { # 특정 고민이 없을 때의 기본 규칙
                    'Dry': [   # 겨울, 기본, 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'Oily': [ # 겨울, 기본, 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','팩폼'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['오일','리치']
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['오일','딥','리치']
                                } 
                        }],
                    'Normal': [ # 겨울, 기본, 중성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationDry': [ # 겨울, 기본, 복합 건성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤','밀크'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','히알루론산','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': []
                                } 
                        }],
                    'CombinationOily': [ # 겨울, 기본, 복합 지성
                        {'title': 'STEP 1. 저녁 세안',
                        'desc': '노폐물을 부드럽게 제거해요.',
                        'query': {
                                    'main_category': '클렌징',
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['오일','밤'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 2. 집중 케어',
                        'desc': '수분과 탄력을 채워요.',
                        'query': {
                                    'middle_category_in': ['에센스/앰플/세럼'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': ['판테놀','나이아신','펩타이드','비타민','병풀','어성초'],
                                    'negative_keywords': []
                                } 
                        },
                        {'title': 'STEP 3. 보습 & 보호',
                        'desc': '건조한 U존을 신경써서 발라주세요.',
                        'query': {
                                    'middle_category_in': ['크림'],
                                    'sub_category_in': ['수분','보습','각질','모공'],
                                    'positive_keywords': [],
                                    'negative_keywords': ['오일','딥']
                                } 
                        }],
                },
            },
        },   
    }