import streamlit as st
from PIL import Image
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows에서 한글 폰트 설정
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지지 않도록 설정

# Set the file paths for the images
image_path_future = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\수소자동차_미래 버전.jpg"
image_path_hybrid1 = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\수소전기 하이브리드_현대 N 비전 74.png"
image_path_hybrid2 = r"C:\Users\Playdata\Desktop\SKN06-1st-1Team-main\Project\streamlit\image\수소전기_하이브리드_N 비전 74.jpg"

st.title("미래의 수소차")

# Display future hydrogen car image
st.subheader("현대 NEXO의 Ai 활용 디자인")
image_future = Image.open(image_path_future)
st.image(image_future, caption='미래 수소자동차', use_column_width=True)

# Display hydrogen hybrid car images
st.subheader("수소 + 전기 하이브리드 - 현대 N 비전 74(양산 예정)")
image_hybrid1 = Image.open(image_path_hybrid1)
st.image(image_hybrid1, caption='현대 N 비전 74', use_column_width=True)

image_hybrid2 = Image.open(image_path_hybrid2)
st.image(image_hybrid2, caption='현대 N 비전 74', use_column_width=True)
