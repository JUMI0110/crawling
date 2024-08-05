import requests
from pprint import pprint
from bs4 import BeautifulSoup # html 코드를 사용할 수 있게 변환해줌

# 크롤링하고 싶은 웹사이트 주소
URL = 'https://dhlottery.co.kr/common.do?method=main'

res = requests.get(URL)

soup = BeautifulSoup(res.text, 'html.parser')


# 1. 특정한 요소를 타겟팅
# balls = soup.select('span.ball_645')

# for ball in balls:
#     print(ball.text)

# 2. 특정한 요소가 없을 때 '+' 형제요소
# print(soup.select('span.bonus + span'))

# 3. 가져오고자하는 데이터가 class와 id가 없을 때 '>' 자식요소 가져올때
# print(soup.select('a#numView > span'))

# 4. a[*="문자열"] a태그가 가지고 있는 속성 중 문자열을 포함하는 요소 가지고 오고 싶을때
# print(soup.select('a[href*="/gameResult"]'))

# 5. 가져오고자하는 데이터 우클릭 copy copy selector