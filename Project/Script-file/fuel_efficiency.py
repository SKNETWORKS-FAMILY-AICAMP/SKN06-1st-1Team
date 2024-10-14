# 연료별 연비 현황 크롤링_open api 활용

import requests
import json
import csv

# API URL 및 인증키 설정
url = 'https://api.odcloud.kr/api/15083023/v1/uddi:399f86ce-69dd-4de3-8b4d-a4fa9c3fa1d8?page=1&perPage=3500'
with open('api_key.json') as fr:    # 인증키 숨김장치
    key_dict = json.load(fr)

key = key_dict['apikey']  
params = {
    'serviceKey': key,  # 인증키
    'pageNo': 1,
    'perPage': 3500,  # 한 페이지에 표시할 데이터 수
}

response = requests.get(url, params=params)

if response.status_code == 200:
    result = response.json()
    all_data = result['data']  # 첫 페이지 데이터 가져오기
else:
    print(f"Error: {response.status_code} - {response.text}")
    all_data = []

# 연료 유형별로 고속도로 연비 값 추출
fuel_types = ['휘발유', '경유', '전기+휘발유', 'LPG', '수소']
fuel_displacement = {fuel: [] for fuel in fuel_types}

# 연료 유형별 고속도로 연비 값 추가
for item in all_data:
    fuel = item.get('연료', '').strip()  # 공백 제거
    if fuel in fuel_displacement and item.get('고속도로연비') is not None:
        try:
            # 고속도로 연비 값을 float로 변환
            fuel_displacement[fuel].append(float(item['고속도로연비']))
        except (ValueError, TypeError):
            continue  # 변환할 수 없는 경우 무시

# 평균값 계산
averages = {}
for fuel in fuel_types:
    if fuel_displacement[fuel]:
        averages[fuel] = sum(fuel_displacement[fuel]) / len(fuel_displacement[fuel])
    else:
        averages[fuel] = 0

# CSV 파일로 저장
csv_filename = 'fuel_efficiency.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # 헤더 작성
    header = ['휘발유', '경유', '전기+휘발유', 'LPG', '수소', '평균값_휘발유', '평균값_경유', '평균값_전기+휘발유', '평균값_LPG', '평균값_수소']
    writer.writerow(header)

    # 평균값을 첫 번째 행에 추가
    averages_row = [f'{averages[fuel]:.2f}' for fuel in fuel_types]
    averages_row.extend([f'{averages[fuel]:.2f}' for fuel in fuel_types])
    writer.writerow(averages_row)

    # 데이터 추가
    max_length = max(len(fuel_displacement[fuel]) for fuel in fuel_types)

    for i in range(max_length):
        row = []
        for fuel in fuel_types:
            value = fuel_displacement[fuel][i] if i < len(fuel_displacement[fuel]) else ''
            row.append(value)

        writer.writerow(row)

print(f"Data saved to {csv_filename} successfully.")
