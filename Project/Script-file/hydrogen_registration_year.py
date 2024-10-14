
# 국내 수소차 등록현황(연도별) 크롤링 후 csv 파일에 저장.

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ChromeDriver 경로 설정 - 각자의 경로 넣어야함
chrome_driver_path = r'C:\Users\Playdata\Documents\chromedriver-win64\chromedriver.exe'

# Service 객체 생성
service = Service(executable_path=chrome_driver_path)

# 웹 드라이버 실행 (크롬)
driver = webdriver.Chrome(service=service)

# 웹사이트 열기
url = "https://www.h2hub.or.kr/main/yard/domestic-hydrogen-vehicle-registration-status-yearly.do"
driver.get(url)

# 페이지가 완전히 로드될 때까지 기다리기
driver.implicitly_wait(10)

# CSV 파일 열기 (쓰기 모드)
with open('hydrogen_registration_year.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # CSV 파일 헤더 작성
    writer.writerow(['연도', '등록 차량 수', '전년 대비 증가량'])

    previous_count = None  # 이전 등록 차량 수를 저장할 변수

    # 'B'부터 'H'까지 순차적으로 선택자 생성하여 크롤링
    for letter in range(ord('B'), ord('H') + 1):  # 'B'부터 'H'까지 반복
        # 선택자 생성
        selector_year = f"#sjs-{chr(letter)}4"
        selector_value = f"#sjs-{chr(letter)}5"

        try:
            # 요소 찾기
            element_year = driver.find_element(By.CSS_SELECTOR, selector_year)
            element_value = driver.find_element(By.CSS_SELECTOR, selector_value)

            # 텍스트 값을 가져와서 정수로 변환
            registration_count = int(element_value.text.replace(',', ''))  # 쉼표 제거 후 정수 변환

            # 전년 대비 증가량 계산
            if previous_count is not None:
                increase = registration_count - previous_count
            else:
                increase = registration_count  # 2018년은 이전 년도 데이터가 없으므로 등록 차량 수 자체를 입력

            # 크롤링한 데이터를 CSV 파일에 작성
            writer.writerow([element_year.text, registration_count, increase])

            # 현재 등록 차량 수를 이전 등록 차량 수로 업데이트
            previous_count = registration_count

        except Exception as e:
            print(f"Element not found for {selector_year} or {selector_value}: {e}")

# 브라우저 닫기
driver.quit()

# 결과 출력
print("Crawled data saved to hydrogen_registration_year.csv successfully.")
