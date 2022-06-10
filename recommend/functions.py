# 맥주 추천 관련 함수 파일
from beer.models import Beer
import csv


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
# return : 가장 유사도가 높은 맥주, 유사도
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

    return max_beer, scores[max_beer]


# beer db 생성 함수
def create_db_beer():
    path = "static/맥주_cbf_data.csv"
    file = open(path, encoding='UTF-8')
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i > 0:
            Beer.objects.create(
                name=row[3],
                style=row[4],
                category=row[5],
                aroma=row[6],
                flavor=row[7],
                balance=row[8],
                season=row[9],
                paring_food=row[10],
                body=row[11],
                rating=row[12],
                img_url=f'images/beer/{row[3]}.png'
            )
    print('Beer DB data created.')


# beer rating 소수점 자르는 함수
def beer_rating_slice():
    beers = Beer.objects.all()
    for beer in beers:
        beer.rating = round(beer.rating, 2)
        beer.save()