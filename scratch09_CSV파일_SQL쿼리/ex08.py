"""
lec08_database 패키지 참고

1) Oracle Database를 연동
2) EMP 테이블의 모든 레코드 SELECT -> 2차원 리스트 생성
3) 생성된 2차원 리스트를 csv 파일(emp.csv)로 저장

ex09.py로...
"""
import cx_Oracle
import lec08_database.oracle_config as cfg
import pandas as pd

# connection 설정
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)


# cursor 객체 생성
cursor = connection.cursor()

# SQL 문장 실행
cursor.execute('select * from emp')
emp = [row for row in cursor ]
print(emp)
print(type(emp))

# cursor 객체 사용 후, 리소스 반환.
cursor.close()

# connection 종료
connection.close()

# 생성된 2차원 리스트를 csv 파일(emp.csv)로 저장
emp = pd.DataFrame(emp)
emp.to_csv('emp.csv', header=False, index=False)