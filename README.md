# <br>💧🔋 **수소차 정보 조회 사이트** 🚗🚌
> **🚘 SK Networks AI CAMP 6기** <br/> **🚘 개발기간: 2024.10.11 ~ 2024.10.15**

<br>

---

<br>

# 🔊 **About us**

<br>

##  **🧬XYCOW🐮** 팀 소개

<br>

| 👋 노원재 | 👋 박서윤 | 👋 정지원 | 👋 홍준 |
|:----------:|:----------:|:----------:|:----------:|
| <img width="200px" src="https://item.kakaocdn.net/do/49a292677e5b578a8985bb315c19700c4022de826f725e10df604bf1b9725cfd" /> | <img width="200px" src="https://item.kakaocdn.net/do/49a292677e5b578a8985bb315c19700c82f3bd8c9735553d03f6f982e10ebe70" /> | <img width="200px" src="https://item.kakaocdn.net/do/49a292677e5b578a8985bb315c19700c960f4ab09fe6e38bae8c63030c9b37f9" /> | <img width="200px" src="https://item.kakaocdn.net/do/49a292677e5b578a8985bb315c19700cb3a18fdf58bc66ec3f4b6084b7d0b570" /> |
| @no1_jae | @y_n1101 | @giana_jw | @bbang__Vl |

<br>

## 🚘 개요 및 소개
> 오늘날 지구 온난화와 대기 오염 문제가 전 세계적으로 중요한 이슈로 부각되며, 탄소 배출을 줄이기 위해 **친환경 차량의 수요가 증가**하고 있습니다. 전기차(EV), 하이브리드 차량, 수소연료전지차(수소차), 바이오연료 등의 친환경 차량이 개발·공급되고 있으며 많은 국가에서 정부 차원의 정책 지원금 혜택을 시행하고 있습니다. 그러나 이런 추세에도 **'수소연료전지차(수소차)'의 수요는 갈 수록 감소**하고 있습니다.<br><br>
> **"수소차의 비인기 이유"** 는 <span style="color: red;"> **"정보 부족"** </span>에서 기인한다고 판단하여 <span style="color: red;">**수소차에 대한 다양한 정보를 제공하는 조회 시스템**</span>을 구축했습니다.
> 
> <br>
> <img width="800px" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN06-1st-1Team/blob/main/Project/image/%EC%88%98%EC%86%8C%EC%B0%A8_%EB%8F%99%EC%9E%91%EC%9B%90%EB%A6%AC.png?raw=true" /> 

<br>

---

<br>

# 🔊 ERD (Entity-Relationship Diagram)

<br>

| <img width="700px" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN06-1st-1Team/blob/main/Project/image/ERD_%EC%99%84%EC%84%B1%EB%B3%B8.png?raw=true" />|
| :--------------------------:|
<br>

---

<br>

# 📝 테이블 정의

<br>

## ✍️ **Type 1**

> - **생성 과정** : csv 파일 형식으로 저장된 데이터를 SQL DATA Base에 저장.
>
> - **구성 요소** (대표 예시 테이블)
>  | 컬럼 명 | 데이터 타입 | 비고 |
| :-------: | :-------: | :-------: |
| 년도 | VARCHAR | - | 
| 전기 | INT | - | 
| 천연가스 | INT | - | 
| 하이브리드 | INT | - | 
| 수소 | INT | - |
| 기타 | INT | - | 
| 합계 | INT | - | 
>
> - **구현 형태** (대표 예시 테이블) <br>
> <br>
> <img width="800px" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN06-1st-1Team/blob/main/Project/image/Type_1.png?raw=true" /> 

<br>

## ✍️ **Type 2**

> - **생성 과정** : 웹 페이지를 크롤링하여 csv 파일 형식으로 저장한 뒤, csv 파일 데이터를 SQL DATA Base에 저장.
>   → <span style="color: blue;">Selenium</span> 활용
>
> - **구성 요소** (대표 예시 테이블)
>
> | 컬럼 명 | 데이터 타입 | 비고 |
| :-------: | :-------: | :-------: |
| 년도 | VARCHAR | - |
| 등록 차량 수 | FLOAT | - |
| 전년 대비 증가량 | FLOAT | - |
>
> - **구현 형태** (대표 예시 테이블) <br>
> <br>
> <img width="800px" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN06-1st-1Team/blob/main/Project/image/Type_2.png?raw=true" /> 

<br>

## ✍️ **Type 3**

> - **생성 과정** : 웹 페이지를 크롤링하여 csv 파일 형식으로 저장한 뒤, csv 파일 데이터를 SQL DATA Base에 저장.
>   → <span style="color: blue;">Open API</span> 활용
>
> - **구성 요소** (대표 예시 테이블)
>
> | 컬럼 명 | 데이터 타입 | 비고 |
| :-------: | :-------: | :-------: |
| 연료 종류 | FLOAT | - |
| 연료 별 주행연비 평균값 | FLOAT | - |
>
> - **구현 형태** (대표 예시 테이블) <br>
> <br>
> <img width="800px" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN06-1st-1Team/blob/main/Project/image/Type_3.png?raw=true" />

<br>

---

<br>

# 🖥 **화면 구성**
<br>
&nbsp;<img width="1000px" src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN06-1st-1Team/blob/main/Project/image/%ED%99%94%EB%A9%B4%20%EA%B5%AC%EC%84%B1.png?raw=true" />

<br>

