"""
with ~ as 구문을 사용하면 connection.close()와 cursor.close()를 자동으로 호출 할 수 있다.
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn: # connection 객체 생성
    with conn.cursor() as cursor: # cursor 객체 생성
        # 실행할 문장
        cursor.execute('select empno, ename, deptno from emp')
        for row in cursor:
            print(row)
            # (7369, 'SMITH', 20)
            # (7499, 'ALLEN', 30)
            # (7521, 'WARD', 30)
            # ...

# ~~~> .close() 없이 자동으로 호출되어 정상 출력 가능
