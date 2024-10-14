import pandas as pd
import pymysql
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

st.title('친환경 연료 사용 차량 연도별 등록 현황')
st.write("SKN_1st_1Team")


# MySQL 연결 설정
connection = pymysql.connect(
    host='localhost',
    user='scott',
    password='tiger',
    database='Project',
)

sql_file_path = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\sql\car_fuel.sql"


try:
    # 테이블에서 데이터 읽기
    query = "SELECT * FROM car_fuel"
    df = pd.read_sql(query, connection)

    # Streamlit으로 데이터프레임 출력
    st.dataframe(df)


    df.set_index('년도', inplace=True)

    #######################################################################
    # 선 그래프 출력
    st.subheader("연도별 연료 사용 현황")
    st.line_chart(df)
################################################################
    ###########################################################
    #막대그래프 출력
    st.bar_chart(df[['수소', '천연가스','하이브리드','전기','기타']])
    #st.line_chart(df[['수소', '']])

   #########################################################################
###################전체에서 수소차 비율 원그래프########################
# Streamlit 제목
#     st.subheader("전체 차량에서 수소차가 자치하는 비율")

# # 파이차트 데이터 (예시)
#     labels = ['수소','전체']
#     values = [36979,4441262]

# # Plotly 파이차트 생성
#     fig = px.pie(
#         names=labels,       # 파이차트에 표시할 항목들
#         values=values,      # 각 항목의 값
#         color=labels,       # 색상은 labels에 따라
#         color_discrete_map={
#             '수소': 'blue', '전체': 'orange'
#         }
#     )
#     fig.update_traces(textfont_size=30) 
#     fig.update_layout(
#         legend=dict( 
#             font_size=30        # 범례 항목 글씨 크기
#         )
#     )
    
# # Streamlit에서 파이차트 출력
#     st.plotly_chart(fig)

###############################################################



finally:
    # 연결 종료
    connection.close()