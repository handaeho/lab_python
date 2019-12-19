"""
사용자에게 입력 받은 내용을 insert 하기
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        # 부서 번호, 이름, 위치를 사용자에게 입력 받음
        deptno = int(input('부서 번호? >>>'))
        dname = input('부서 이름? >>>')
        loc = input('부서 위치? >>>')

        # 여기서 insert에 들어가는 변수를 위해 formatted string 형태로 사용해야 한다.
        # 또한 deptno말고는 문자 형태로 입력 받기 때문에 ''로 묶어주어야 한다.
        sql_insert = f"insert into dept2 values({deptno}, '{dname}', '{loc}')"
        # 이 형태로 insert를 하게 되면, 문제가 있다.
        # 현재 사용자에게 입력 받은 문자를 insert 할 때, ''로 묶었는데
        # 만약 사용자가 입력한 문자에 ''이 포함 되어 있으면 에러가 발생한다. 위의 방법은 권장 X
        # 따라서 'Data Binding'을 사용해야 한다. ~~~> ex06.py 참고

        # insert 실행
        cursor.execute(sql_insert)

        # commit(변경 사항 영구 반영)
        conn.commit()

        # 확인 위한 select
        sql_select = 'select * from dept2'
        cursor.execute(sql_select)
        for row in cursor:
            print(row)

