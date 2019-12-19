"""
select(검색) 문 : oracle 데이터 베이스 서버에서 select 구문 실행, 결과 확인

<기본 순서>
connection 설정 -> cursor 객체 생성 -> cursor 객체 사용 후, 리소스 반환 -> connection 종료
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

# 데이터베이스 서버와 연결 - 접속(로그인)
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)

# 접속한 데이터베이스 버전 정보
print('DB Server : ', connection.version) # DB Server :  11.2.0.1.0

# SQL 문장 실행 위한 'cursor' 객체 생성
cursor = connection.cursor()

# SQL 문장 실행
cursor.execute('select * from emp')
while True:
    row = cursor.fetchone() # select의 결과에서 한 행(row)의 결과를 읽어온다.
    if row is None: # select의 결과가 더 이상 없으면,
        break
    print(row)
    # SQL 서버의 emp 테이블 결과를 모두 출력
    # (7369, 'SMITH', 'CLERK', 7902, datetime.datetime(1980, 12, 17, 0, 0), 800.0, None, 20)
    # (7499, 'ALLEN', 'SALESMAN', 7698, datetime.datetime(1981, 2, 20, 0, 0), 1600.0, 300.0, 30)
    # (7521, 'WARD', 'SALESMAN', 7698, datetime.datetime(1981, 2, 22, 0, 0), 1250.0, 500.0, 30)
    # (7566, 'JONES', 'MANAGER', 7839, datetime.datetime(1981, 4, 2, 0, 0), 2975.0, None, 20)
    # ...

# 아니면 이렇게도 가능
row = cursor.fetchone() # select의 결과에서 한 행(row)의 결과를 읽어온다.
while row: # 읽은 행(row)의 데이터가 있다면
    print(row) # 각 행의 레코드가 있는 tuple 형태
    row = cursor.fetchone() # 그 다음 행을 또 읽어온다.

# cursor 객체 사용 후, 리소스 반환
cursor.close()

# 데이터베이스 서버와 연결 종료
connection.close()

