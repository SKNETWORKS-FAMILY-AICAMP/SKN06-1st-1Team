import pymysql
import pandas as pd
import os

def csv_to_sql(csv_file_name, table_name):
    
    root_path = os.path.dirname(os.path.abspath(__file__))
    
    # CSV 파일 경로 설정
    csv_file_path = os.path.join(root_path, 'data', csv_file_name)
    
    # CSV 파일 읽기
    df = pd.read_csv(csv_file_path, encoding='utf-8-sig')
    
    # SQL 파일 경로 설정
    sql_file_path = os.path.join(root_path, 'sql', f'{table_name}.sql')
    
    try:
        # SQL 파일에 INSERT INTO 문 생성 및 저장
        with open(sql_file_path, 'w', encoding='utf-8') as f:
            # 테이블 생성 SQL 문을 생성하는 부분 (필요에 따라 수정)
            create_table = f"CREATE TABLE {table_name} (\n"
            for column in df.columns:
                create_table += f"    {column} VARCHAR(255),\n"
            create_table = create_table.rstrip(',\n') + '\n);\n\n'
            f.write(create_table)
            
            # INSERT INTO 문을 생성하여 SQL 파일에 추가
            for i, row in df.iterrows():
                sql = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ("
                sql += ', '.join([f"'{str(x)}'" if pd.notna(x) else 'NULL' for x in row.values])
                sql += ");\n"
                f.write(sql)
        print(f"SQL 파일이 성공적으로 저장되었습니다: {sql_file_path}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    # 사용 예시: 사용자가 CSV 파일 이름과 테이블 이름을 입력하면 해당 데이터를 SQL 파일로 저장합니다.
    # 예를 들어, 'hydrogen_car.csv' 파일을 'hydrogen_car' 테이블로 저장하려면 파일 이름과 테이블 이름을 입력하면 됩니다.
    csv_file_name = input("CSV 파일 이름을 입력하세요 (예: hydrogen_car.csv): ")
    table_name = input("SQL로 저장할 테이블 이름을 입력하세요: ")
    csv_to_sql(csv_file_name, table_name)