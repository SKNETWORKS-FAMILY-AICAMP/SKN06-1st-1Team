
# 지역별 수소차 등록 현황 (기준: 2024.08)

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ChromeDriver 경로 설정
chrome_driver_path = r'C:\Users\Playdata\Documents\chromedriver-win64\chromedriver.exe'

# Service 객체 생성
service = Service(executable_path=chrome_driver_path)

# 웹 드라이버 실행 (크롬)
driver = webdriver.Chrome(service=service)

# 웹사이트 열기
url = "https://www.h2hub.or.kr/main/stat/stat_use_hCar_apply.do"
driver.get(url)

# 페이지가 완전히 로드될 때까지 기다리기
driver.implicitly_wait(10)

# 크롤링한 데이터를 CSV 파일에 저장
csv_file = 'hydrogen_registration_region.csv'

try:
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # CSV 파일의 헤더(열 제목) 작성
        writer.writerow(['지역', '차량 수'])

        # 'C'부터 'T'까지 순차적으로 선택자 생성
        for letter in range(ord('C'), ord('T') + 1):  # 'C'부터 'T'까지 반복
            # 선택자 생성
            selector_region = f"#sjs-{chr(letter)}4"
            selector_count = f"#sjs-{chr(letter)}19"

            try:
                # 요소 찾기
                element_region = driver.find_element(By.CSS_SELECTOR, selector_region)
                element_count = driver.find_element(By.CSS_SELECTOR, selector_count)

                # 쉼표 제거 후 정수형으로 변환
                registration_count = int(element_count.text.replace(',', ''))  
                
                # 크롤링한 데이터를 CSV 파일에 저장
                writer.writerow([element_region.text, registration_count])

            except Exception as e:
                print(f"Element not found for {selector_region} or {selector_count}: {e}")
                
except Exception as e:
    print(f"Error while saving data to CSV: {e}")
    
finally:
    # 브라우저 닫기
    driver.quit()

# 결과 출력
print(f"Crawled data saved to {csv_file} successfully.")
