import csv
import json
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

# movie_dict를 ./data/weekly.json 저장
# 재사용성을 위해서 변수에 저장
output_dir = './data'
output_file = os.path.join(output_dir, 'weekly.json')
# output_file = os.path.join(output_dir, 'weekly.json')
# 경로가 있는지 없는지 True/False
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# [f = open()] with open을 통해서 파일을 열면 with문이 끝날 시 파일 닫음
# 'w' 옵션 write 
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(movie_dict, f, ensure_ascii=False)
    # python dict를 json으로 바꾸는 함수(dict, 넣을 파일이름)
   
# movie_dict를 ./data/weekly.csv로 저장

output_file = os.path.join(output_dir, 'weekly.csv')

with open(output_file, 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['대표코드', '영화명', '누적관객수'])
    # 컬럼의 이름 작성
    for movie in movie_list:
        csv_writer.writerow([movie['movieCd'], movie['movieNm'], movie['audiAcc']])
