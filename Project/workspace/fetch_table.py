import pymysql
import pandas as pd
from db_connect import db_connect


def fetch_table(table_name):
    connection = db_connect()
    if connection:
        try:
            # SQL 쿼리 실행하여 데이터를 가져옴
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, connection)
            print(f"{table_name} 테이블의 데이터를 성공적으로 불러왔습니다.")
            print(df)
        except Exception as e:
            print(f"데이터를 불러오는 중 오류가 발생했습니다: {e}")
        finally:
            connection.close()

if __name__ == "__main__":
    table_name = input("불러올 테이블 이름을 입력하세요: ")
    fetch_table(table_name)