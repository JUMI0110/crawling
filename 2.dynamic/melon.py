from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # 기준점설정 라이브러리
import os
import time 

# os 모듈 운영체제의 경로를 다룰 수 있게 해주는 모듈
# path 경로관련 설정 라이브러리
# abspath 절대경로 (시작부터 끝) __file__ 파일 기준
# 현재 폴더를 변수에 담아 어디서든 쓸 수 있게 설정
currunt_folder = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(currunt_folder, 'chromedriver.exe')

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

URL = 'https://www.melon.com/chart/index.htm'

driver.get(URL)
# time.sleep(3) # 3초 멈춤

song_info = driver.find_elements(By.CSS_SELECTOR, 'a.btn.button_icons.type03.song_info') # 조건에 맞는 요소 찾기

for i in range(5):
    song_info[i].click() 
    time.sleep(2)
    
    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text
    
    song_meta = driver.find_element(By.CSS_SELECTOR, 'dl.list')
    
    for child in song_meta.find_elements(By.CSS_SELECTOR, 'dt, dd'):
        if child.tag_name == 'dt':
            print(child.text, end=':')
        else:
            print(child.text)

    like_cnt = driver.find_element(By.CSS_SELECTOR, 'span#d_like_count').text
    print(like_cnt)
    

    driver.back() # 뒷페이지로
