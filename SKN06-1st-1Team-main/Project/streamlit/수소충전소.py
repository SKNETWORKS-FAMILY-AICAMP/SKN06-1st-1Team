import pandas as pd
import pymysql
import streamlit as st
import plotly.graph_objects as go

st.title('전국 수소 충전소 현황⚡')
st.write("전국 수소 충전소 설치 현황")

# MySQL 연결 설정
connection = pymysql.connect(
    host='localhost',
    user='scott',
    password='tiger',
    database='Project'
)

sql_file_path = r'C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\sql\hydrogen_station.sql'

try:
    # 테이블에서 데이터 읽기
    query = "SELECT * FROM hydrogen_station"
    df = pd.read_sql(query, connection)

    # 문자열로 된 열을 숫자로 변환 (필요한 경우에 따라 열 이름을 변경하세요)
    for column in ['위도', '경도']:  # 숫자 연산이 필요한 열을 지정합니다.
        df[column] = pd.to_numeric(df[column], errors='coerce')

    ####################전국 수소차 충전소 등록 현황 차트#################################################
    # Streamlit으로 데이터프레임 출력
    st.dataframe(df)

    # 두 개의 그래프를 나란히 배치하기 위해 st.columns 사용
    col1, col2 = st.columns(2)  # 두 개의 열 생성

    with col1:
        # 지도 출력
        st.write("**전국 수소충전소 분포도⚡**")
        st.map(df, latitude='위도', longitude='경도')

    with col2:
        ################################전국 수소차 등록 현황 버블차트#######################################################3
        # 지역 정보 (위도, 경도, 크기, 색상 등)
        locations = {
            "서울": {"lat": 37.5665, "lon": 126.9780, "size": 3270 / 50, "color": 3270 / 100},
            "부산": {"lat": 35.1796, "lon": 129.0756, "size": 2115 / 50, "color": 2115 / 100},
            "대구": {"lat": 35.8714, "lon": 128.6014, "size": 673 / 50, "color": 673 / 100},
            "인천": {"lat": 37.4563, "lon": 126.7052, "size": 2324 / 50, "color": 2324 / 100},
            "광주": {"lat": 35.1595, "lon": 126.8514, "size": 1253 / 50, "color": 1253 / 100},
            "대전": {"lat": 36.3504, "lon": 127.3845, "size": 1812 / 50, "color": 1812 / 100},
            "울산": {"lat": 35.5384, "lon": 129.3114, "size": 2951 / 50, "color": 2951 / 100},
            "세종": {"lat": 36.4803, "lon": 127.2895, "size": 500 / 50, "color": 500 / 100},
            "경기": {"lat": 37.4138, "lon": 127.5183, "size": 7970 / 50, "color": 7970 / 100},
            "강원": {"lat": 37.8228, "lon": 128.1555, "size": 2731 / 50, "color": 2731 / 100},
            "충북": {"lat": 36.6355, "lon": 127.9202, "size": 2235 / 50, "color": 2235 / 100},
            "충남": {"lat": 36.5784, "lon": 126.9910, "size": 1707 / 50, "color": 1707 / 100},
            "전북": {"lat": 35.7195, "lon": 127.1397, "size": 2556 / 50, "color": 2556 / 100},
            "전남": {"lat": 34.8167, "lon": 126.4580, "size": 1177 / 50, "color": 1177 / 100},
            "경북": {"lat": 36.5761, "lon": 128.1382, "size": 508 / 50, "color": 508 / 100},
            "경남": {"lat": 35.4605, "lon": 128.2132, "size": 2955 / 50, "color": 2955 / 100},
            "제주": {"lat": 33.4996, "lon": 126.5312, "size": 50 / 50, "color": 50 / 100},
        }

        # 데이터 준비
        latitudes = [loc["lat"] for loc in locations.values()]
        longitudes = [loc["lon"] for loc in locations.values()]
        sizes = [loc["size"] for loc in locations.values()]
        colors = [loc["color"] for loc in locations.values()]
        city_names = list(locations.keys())

        # Mapbox 토큰 (무료 계정으로 생성 가능)
        mapbox_access_token = "YOUR_MAPBOX_ACCESS_TOKEN"  # 여기에 자신의 Mapbox 토큰을 넣어주세요.

        # 지도 위에 버블 차트 생성
        fig = go.Figure(go.Scattermapbox(
            lat=latitudes,
            lon=longitudes,
            mode='markers',
            marker=dict(
                size=sizes,  # 버블 크기
                color=colors,  # 버블 색상
                colorscale='Viridis',  # 색상 스케일
                showscale=True,  # 색상 표시
                opacity=0.7
            ),
            text=city_names,  # 툴팁에 표시될 텍스트 (도시 이름)
            hoverinfo="text"
        ))

        # 지도 설정
        fig.update_layout(
            title="전국 수소차 분포도💧🚙",
            mapbox=dict(
                style="open-street-map",  # OpenStreetMap 스타일
                center=dict(lat=36.5, lon=128),  # 지도 중심 좌표
                zoom=5.3,  # 확대 수준
                accesstoken=mapbox_access_token  # Mapbox 액세스 토큰 설정
            )
        )

        # Streamlit에서 그래프 출력
        st.plotly_chart(fig)

finally:
    # 연결 종료
    connection.close()
