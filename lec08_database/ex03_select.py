"""
for ~ in 반복문을 이용한 select문 결과 처리

<형태>
for 변수 in cursor:
    실행문

= for ~ in 구문에서 cursor.fetchone()의 결과를 변수에 전달. fetchone() 필요없이 같은 결과를 출력한다.
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

# connection 설정
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)


# cursor 객체 생성
cursor = connection.cursor()

# SQL 문장 실행
cursor.execute('select * from emp')
for row in cursor: # fetchone() 필요 없이, SQL 문장 실행 후, cursor 객체에 들어온 행(row) 수 만큼 출력
    print(row)

# cursor 객체 사용 후, 리소스 반환.
cursor.close()

# connection 종료
connection.close()
