import streamlit as st
from PIL import Image
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows에서 한글 폰트 설정
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지지 않도록 설정

# Set the file paths for the images
image_path_front = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\nexo_front.jpg"
image_path_back = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\nexo_back.jpg"
image_path_bus = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\수소버스.jpg"
image_path_principle = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\수소자동차 작동 원리.jpg"

# 페이지 제목
st.title("🌼SKN_1st_1Team - XYCOW🐄🐮")
st.write("조원 : **🐼🐼노원재 박서윤 정지원 홍준🐼🐼**")

# Create a Streamlit application to display the images and information
def main():
    # 수소자동차 작동 원리 이미지 및 설명
    st.title("**수소자동차란?💧+🔋=🚙**")
    st.write("<p>수소차는 수소와 산소를 화학 반응시켜 전기를 생성하고, 이를 통해 차량의 모터를 구동합니다.</p><p><수소 공급> - <산소 공급> - <화학 반응> - <전기 생산> - <물 배출> 의 순서로 작동하며, 가스 배출 없이 물만 배출하기 때문에 대기 오염을 유발하지 않는 친환경 차량입니다.</p>",
            unsafe_allow_html=True
        )
    
    # Load the image using PIL and display it in Streamlit
    image_principle = Image.open(image_path_principle)
    st.image(image_principle, caption='수소자동차 작동 원리💧+🔋=🚙', use_column_width=True)



    
    # 수소자동차 이미지들
    st.title("수소자동차")
    st.write("국내 유일 수소차 - 현대자동차 NEXO")
    
    # Load the images using PIL and resize them
    image_front = Image.open(image_path_front)
    image_back = Image.open(image_path_back)
    image_bus = Image.open(image_path_bus)
    image_front = image_front.resize((810, 450))
    image_back = image_back.resize((810, 450))
    image_bus = image_bus.resize((770, 474))
    
    # Display the images in Streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.image(image_front, caption='Nexo - Front View', use_column_width=True)
    with col2:
        st.image(image_back, caption='Nexo - Back View', use_column_width=True)

    st.image(image_bus, caption='Hydrogen Bus', use_column_width=True)



    st.write("**자동차 사용 연료별 연비 (고속주행시)**")

    # MySQL 연결 설정
    connection = pymysql.connect(
        host='localhost',
        user='scott',
        password='tiger',
        database='Project'
    )

    try:
        # 테이블에서 데이터 읽기
        query = "SELECT * FROM fuel_efficiency"
        df = pd.read_sql(query, connection)
        # 필요한 열만 선택
        selected_columns = ['평균값_휘발유', '평균값_경유', '평균값_전기+휘발유', '평균값_LPG', '평균값_수소']
        df_selected = df[selected_columns]
        first_row = df_selected.iloc[0]  # 첫 번째 행을 선택

        # 각 연료별 평균값 계산 (하나의 값만 존재한다고 가정)
        df_selected_mean = df_selected.iloc[0]

        # 첫 번째 행만 선택하여 막대그래프 생성
        fig, ax = plt.subplots(figsize=(10, 6))

        # 막대그래프 그리기 (가로 방향)
        ax.barh(first_row.index, first_row.values, color=['red', 'green', 'purple', 'orange', 'blue'])

        custom_labels = ['휘발유', '경유', '전기+휘발유', 'LPG', '수소']
        ax.set_yticklabels(custom_labels)
        
        # 항목 이름 변경 (x축 레이블, y축 레이블 수정)
        ax.set_title("연료별 평균 연비")
        ax.set_xlabel("평균 연비")
        ax.set_ylabel("연료 종류")

        # 값 레이블 추가 (각 막대 위에 값 표시)
        for i, value in enumerate(first_row.values):
            ax.text(value + 0.1, i, f'{value:.2f}', va='center')

        # Streamlit에 matplotlib 그래프 표시
        st.pyplot(fig)
    finally:
        # 연결 종료
        connection.close()

# 사이드바에 페이지 선택 메뉴 추가
st.sidebar.title("목차")
if st.sidebar.button("수소차란 ? ", key='main_page_button'):
    main()
# if st.sidebar.button("자동차 증가량", key='car_growth_button'):
#     exec(open("자동차 증가량.py", encoding='utf-8').read())
if st.sidebar.button("수소차 등록 현황", key='hydrogen_car_status_button'):
    exec(open("수소차 등록 현황.py", encoding='utf-8').read())
if st.sidebar.button("수소충전소 현황", key='hydrogen_station_info_button'):
    exec(open("수소충전소.py", encoding='utf-8').read())
if st.sidebar.button("친환경 차량 등록 현황", key='fuel_car_status_button'):
    exec(open("연료별 자동차 등록 현황.py", encoding='utf-8').read())
if st.sidebar.button("미래의 수소차", key='why_hydrogen_unpopular_button'):
    exec(open("수소차가 인기없는 이유.py", encoding='utf-8').read())


# 목차 버튼 추가
if st.button('시스템 설명'):
    st.subheader("수소차 관련 정보 조회 시스템입니다.")
    st.write(
        "<p>오늘날 지구 온난화와 대기 오염 문제는 전 세계적으로 중요한 이슈로 부각되고 있으며, 탄소 배출을 줄이기 위한 친환경 차량의 수요가 증가하고 있습니다. 전기(EV), 하이브리드, 수소연료전지 등을 활용한 친환경 차량이 개발되었고, 활성화를 위해 많은 국가에서 정부 차원의 정책 지원금 혜택을 제공하고 있습니다.</p><p>그러나 이러한 친환경 차량의 성장에도 불구하고, 수소차의 수요는 점차 감소하고 있습니다. 이는 수소차에 대한 정보 부족이 주요 원인 중 하나입니다. 이에 따라 수소차의 국내 현황과 상용화의 어려움을 이해하고 개선하기 위한 정보 조회 시스템을 구축했습니다.</p>",
        unsafe_allow_html=True
    )