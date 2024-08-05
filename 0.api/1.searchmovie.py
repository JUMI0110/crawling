import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
KOBIS_API_KEY = os.getenv('KOBIS_API_KEY')

URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'

SEARCH_MOVIE_URL = f'{URL}?key={KOBIS_API_KEY}&movieCd='

input_dir = './data'
input_file = os.path.join(input_dir, 'weekly.json')

with open(input_file, 'r', encoding='utf-8') as f:
    movie_dict = json.load(f)
    # json 파일을 dict형태로 가져오기

for movie_cd in movie_dict.keys():
    SM_URL = SEARCH_MOVIE_URL + movie_cd

    res = requests.get(SM_URL)
    data = res.json()

    actors = data['movieInfoResult']['movieInfo']['actors']
    actor_str = ', '.join([actor['peopleNm'] for actor in actors ])
    print(actor_str)