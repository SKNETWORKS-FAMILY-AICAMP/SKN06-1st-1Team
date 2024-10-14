import pymysql
import pandas as pd
import os

def sql_to_csv(table_name):
    # 데이터베이스 연결 설정
    connection = pymysql.connect(
        host="127.0.0.1",
        user='scott',
        password='tiger',
        db='project'
    )

    try:
        # 사용자가 입력한 테이블 이름을 사용하여 SQL 쿼리 실행
        df = pd.read_sql(f"SELECT * FROM {table_name}", connection)

        # CSV 파일 경로 설정
        csv_path = os.path.join('SKN06-1st-1Team-main', 'data', f'{table_name}.csv')
        
        # 데이터를 CSV 파일로 저장
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"CSV 파일이 성공적으로 저장되었습니다: {csv_path}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    finally:
        # 연결 닫기
        connection.close()

if __name__ == "__main__":
    table_name = input("CSV로 내보낼 테이블 이름을 입력하세요: ")
    sql_to_csv(table_name)