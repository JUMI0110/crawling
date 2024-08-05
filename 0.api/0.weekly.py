import os
import requests
from dotenv import load_dotenv
# .env 안의 KEY 가져오기 
load_dotenv()
KOBIS_API_KEY = os.getenv('KOBIS_API_KEY')

URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'


WEEKLY_URL = f'{URL}?key={KOBIS_API_KEY}&targetDt=20240701'

res = requests.get(WEEKLY_URL)
data = res.json()
# json 구조를 딕셔너리 형태로 변환

movie_list = data['boxOfficeResult']['weeklyBoxOfficeList']


movie_dict = {}

for movie in movie_list:
    movie_dict[movie['movieCd']] = {
        '영화명': movie['movieNm'],
        '누적관객수': movie['audiAcc']
    }
print(movie_dict)   