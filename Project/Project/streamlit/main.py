import streamlit as st
from PIL import Image

# 페이지 제목
st.title("🌼SKN_1st_1Team - XYCOW🐄🐮")
st.write("조원 : **🐼🐼노원재 박서윤 정지원 홍준🐼🐼**")

import streamlit as st
from PIL import Image

# Set the file path for the image
image_path = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\수소자동차 작동 원리.jpg"

# Create a Streamlit application to display the image
def main():
    st.title("**수소자동차란?💧+🔋=🚙**")
    st.write("<p>수소차는 수소와 산소를 화학 반응시켜 전기를 생성하고, 이를 통해 차량의 모터를 구동합니다.</p><p><수소 공급> - <산소 공급> - <화학 반응> - <전기 생산> - <물 배출> 의 순서로 작동하며, 가스 배출 없이 물만 배출하기 때문에 대기 오염을 유발하지 않는 친환경 차량입니다.</p>",
            unsafe_allow_html=True
        )
    
    # Load the image using PIL and display it in Streamlit
    image = Image.open(image_path)
    st.image(image, caption='수소자동차 작동 원리💧+🔋=🚙', use_column_width=True)

# 사이드바에 페이지 선택 메뉴 추가
# page = st.sidebar.selectbox(
#     "목차",
#     ("메인 페이지", "자동차 증가량", "수소차 등록 현황", "수소충전소 정보", "연료별 자동차 등록 현황", "수소차가 인기없는 이유")
# )

# 페이지에 따른 내용 표시
st.sidebar.title("목차")
if st.sidebar.button("메인 페이지", key='main_page_button'):
    st.header("수소차 등록 정보 시스템")
    st.write(
        "<p>오늘날 지구 온난화와 대기 오염 문제가 전 세계적으로 중요한 이슈로 부각되며, 탄소 배출을 줄이기 위해 친환경 차량의 수요가 증가하고 있습니다. 전기차(EV), 하이브리드 차량, 수소연료전지차(수소차), 바이오연료 등의 친환경 차량이 개발·공급되고 있으며 많은 국가에서 정부 차원의 정책 지원금 혜택을 시행하고 있습니다.</p><p>그러나 이런 추세에도 '수소연료전지차(수소차)'의 수요는 갈 수록 감소하고 있습니다. '수소차는 왜 상용화에 실패했을까' 라는 질문에 답하기 위해 수소차의 국내 현황 및 상용화 실패 이유에 대한 정보 조회 시스템을 구축했습니다.</p>",
        unsafe_allow_html=True
    )
    main()
# if st.sidebar.button("자동차 증가량", key='car_growth_button'):
#     exec(open("자동차 증가량.py", encoding='utf-8').read())
if st.sidebar.button("수소차 등록 현황", key='hydrogen_car_status_button'):
    exec(open("수소차 등록 현황.py", encoding='utf-8').read())
if st.sidebar.button("수소충전소 정보", key='hydrogen_station_info_button'):
    exec(open("수소충전소.py", encoding='utf-8').read())
if st.sidebar.button("친환경 차량 사용 현황", key='fuel_car_status_button'):
    exec(open("연료별 자동차 등록 현황.py", encoding='utf-8').read())
if st.sidebar.button("수소차 상용화 실패 사유", key='why_hydrogen_unpopular_button'):
    exec(open("수소차가 인기없는 이유.py", encoding='utf-8').read())


# 목차 버튼 추가
if st.button('메인페이지로 이동'):
    st.write("### 소개")
    st.write("이 프로젝트는 수소차와 관련된 다양한 데이터를 분석하고 시각화하는 것을 목표로 합니다.")
