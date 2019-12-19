"""
Data Binding을 사용한 SQL 문장 실행

Data Binding = Oracle에서 SQL 문장 실행 시, 권장되는 방법.
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호? >>>'))
        dname = input('부서 이름? >>>')
        loc = input('부서 위치? >>>')

        # data binding

        # 첫번째 방법 => 인덱스 번호를 주고, 파라미터로 리스트를 넘겨준다.
        sql1 = 'insert into dept2 values(:0, :1, :2)'
        cursor.execute(sql1, [deptno, dname, loc]) # 실행할 때 2번째 파라미터로 리스트를 넘겨준다
        # 전달받은 리스트의 index 0번(:0)으로 채우고, 1번(:1)으로 채우고, 2번(:2)으로 채우겠다.
        # :0 ~> deptno, :1 ~> dname, :2 ~> loc
        # 숫자면 숫자, 문자면 문자가 자동으로 들어감.

        # 두번째 방법 => keyword argument를 사용한다.
        sql2 = 'insert into dept2 values(:dept_no, :dept_name, :loc)'
        cursor.execute(sql2, dept_no=deptno, dept_name=dname, loc=loc)
        connection.commit()

        # 확인 위한 select
        sql_select = 'select * from dept2'
        cursor.execute(sql_select)
        for row in cursor:
            print(row)
            # ...
            # (22, "a'b'c", "seoul's") ~~~> 입력한 문자열에 ''가 있어도 정상적으로 insert 된다.

