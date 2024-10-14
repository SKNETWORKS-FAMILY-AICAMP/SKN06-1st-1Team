import pandas as pd
import pymysql
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.title('연도별 수소자동차 등록 현황')
st.write("SKN_1st_1Team")


# MySQL 연결 설정
connection = pymysql.connect(
    host='localhost',
    user='scott',
    password='tiger',
    database='Project',
)

sql_file_path = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\sql\hydrogen_registration_year.sql"


try:
    query = "SELECT * FROM hydrogen_registration_year"
    df = pd.read_sql(query, connection)
    st.dataframe(df)

    ####################연도별 수소차 등록 현황 차트#################################################
    # 연도별 데이터를 처리
    df['연도'] = df['연도'].astype(str)  # 연도를 문자열로 변환
    
    # Plotly 그래프 만들기
    fig = go.Figure()

    # 전년 대비 증가량을 막대그래프로 추가
    fig.add_trace(go.Bar(
        x=df['연도'],  # 연도
        y=df['전년 대비 증가량'],  # 전년 대비 증가량
        name='전년 대비 증가량',
        marker=dict(color='skyblue')
    ))

    # 등록 차량 수를 꺾은선 그래프로 추가
    fig.add_trace(go.Scatter(
        x=df['연도'],  # 연도
        y=df['등록 차량 수'],  # 등록 차량 수
        name='등록 차량 수',
        mode='lines+markers',  # 꺾은선 그래프 + 마커 표시
        line=dict(color='green', width=2),
        marker=dict(size=8, color='green')
    ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title='연도별 수소차 등록 현황',
        xaxis_title='연도',
        yaxis_title='차량 수',
        barmode='group',  # 막대그래프와 꺾은선 그래프를 그룹으로 표시
        legend_title='그래프 항목'
    )

    # 그래프 출력
    st.plotly_chart(fig)


    
    st.subheader("전체 차량에서 수소차가 자치하는 비율")

# 파이차트 데이터 (예시)
    labels = ['수소','전체']
    values = [36979,4441262]

# Plotly 파이차트 생성
    fig = px.pie(
        names=labels,       # 파이차트에 표시할 항목들
        values=values,      # 각 항목의 값
        color=labels,       # 색상은 labels에 따라
        color_discrete_map={
            '수소': 'blue', '전체': 'orange'
        }
    )
    fig.update_traces(textfont_size=30) 
    fig.update_layout(
        legend=dict( 
            font_size=30        # 범례 항목 글씨 크기
        )
    )
    
# Streamlit에서 파이차트 출력
    st.plotly_chart(fig)

finally:
    # 연결 종료
    connection.close()