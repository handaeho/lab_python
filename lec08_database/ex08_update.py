"""
Update
수정할 부서 번호를 입력받아, 그 부서의 위치를 수정하는 update문을 만들어 보자.
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = input('부서 번호? >>> ')
        loc = input('수정할 위치? >>> ')

        sql1 = 'update dept2 set loc = :loc where deptno = :deptno'
        cursor.execute(sql1, deptno=deptno, loc=loc)
        connection.commit()

        sql_select = 'select * from dept2'
        cursor.execute(sql_select)
        for row in cursor:
            print(row)
            # ...
            # (22, 'ABC', 'lisan')
            # (22, "a'b'c", 'lisan')