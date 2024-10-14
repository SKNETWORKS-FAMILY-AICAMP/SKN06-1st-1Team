import pymysql

# MySQL 데이터베이스 연결 설정
def db_connect():
    try:
        connection = pymysql.connect(
            host="127.0.0.1",    # MySQL 호스트
            user="scott",  # MySQL 사용자
            password="tiger",  # MySQL 비밀번호
            db="Project",  # 연결할 MySQL 데이터베이스
            charset='utf8mb4',   # 인코딩을 위한 문자셋
            cursorclass=pymysql.cursors.DictCursor  # 행을 딕셔너리 형태로 반환
        )
        print("데이터베이스 연결에 성공했습니다.")
        return connection
    except Exception as e:
        print(f"데이터베이스 연결에 실패했습니다: {e}")
        return None

if __name__ == "__main__":
    # 데이터베이스 연결
    connection = db_connect()
    if connection:
        connection.close()