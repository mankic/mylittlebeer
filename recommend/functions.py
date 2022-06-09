# 맥주 추천 관련 함수 파일
from beer.models import Beer


# 문자열 형태의 맥주 특징을 리스트 형태로 파싱하는 함수
# array_str : 문자열 형태의 맥주 특성
# return : 리스트 형태의 맥주 특성
def list_parser(array_str):
    try:
        temp = array_str[1:-1].split(', ')
        for i in range(len(temp)):
            temp[i] = temp[i][1:-1]
    except:
        temp = array_str
    return temp


# 두 리스트의 유사도를 측정하는 자카드 유사도 함수
# list_1, list_2 : 유사도를 측정하는 두 리스트
# return : 두 리스트의 유사도 비율
def jaccard_similarity(list_1, list_2):
    union = list(set(list_1) | set(list_2))
    intersection = list(set(list_1) & set(list_2))
    return len(intersection) / len(union)


# 입력받은 맥주 특성과 유사도가 비슷한 맥주를 찾는 함수
# user_beer : 유저가 선호하는 맥주 특징
# return : 가장 유사도가 높은 맥주
def find_favorite_beer(user_beer):
    features = ['style', 'category', 'aroma', 'flavor', 'season', 'paring_food', 'body']
    base_beer = user_beer
    beers = Beer.objects.all()
    scores = {}

    # 맥주 별
    for beer in beers:
        score = 0
        for i, feature in enumerate(features):
            # style, category : 같은 지 확인
            if i < 2:
                if base_beer[i] == getattr(beer, feature):
                    ratio = 0.3
                else:
                    ratio = 0
            # 나머지 특징 : 문자열 형태를 리스트 형태로 바꾼뒤 자카드 유사도로 측정
            else:
                list_feature = list_parser(getattr(beer, feature))
                ratio = jaccard_similarity(base_beer[i], list_feature)

            score += 10 * ratio

        scores[beer.name] = round(score, 2)

    max_beer = max(scores, key=scores.get)

    return max_beer
