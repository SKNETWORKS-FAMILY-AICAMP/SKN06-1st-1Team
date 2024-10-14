import streamlit as st
from PIL import Image
import pandas as pd
import pymysql

st.title('수소차가 인기없는 이유')
st.write("**연료별 자동차 연비**")

# MySQL 연결 설정
connection = pymysql.connect(
    host='localhost',
    user='scott',
    password='tiger',
    database='Project'
)

sql_file_path = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\sql\fuel_efficiency.sql"

try:
    # 테이블에서 데이터 읽기
    query = "SELECT * FROM fuel_efficiency"
    df = pd.read_sql(query, connection)
    # Streamlit으로 데이터프레임 출력
    st.dataframe(df)
finally:
    # 연결 종료
    connection.close()

# Set the file paths for the images
image_path_front = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\nexo_front.jpg"
image_path_back = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\nexo_back.jpg"
image_path_bus = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\수소버스.jpg"

# Create a Streamlit application to display the image
def main():
    st.title("수소자동차")
    st.write("국내 유일 상용수소차 - 현대자동차 NEXO")
    
    # Load the image using PIL and resize it
    image_front = Image.open(image_path_front)
    image_back = Image.open(image_path_back)
    image_bus = Image.open(image_path_bus)
    image_back = image_back.resize((810, 450))
    image_bus = image_bus.resize((770, 474))
    
    # Display the image in Streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.image(image_front, caption='Nexo - Front View', use_column_width=True)
    with col2:
        st.image(image_back, caption='Nexo - Back View', use_column_width=True)

    st.image(image_bus, caption='Hydrogen Bus', use_column_width=True)

main()