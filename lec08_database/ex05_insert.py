"""
insert 문 사용
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

# with ~ as 구문으로 데이터베이스 서버와 연결 설정
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    # SQL 문장을 실행하고, 결과를 분석할 수 있는 cursor 객체 생성
    with connection.cursor() as cursor:
        # insert문 안의 문자열은 ''로 묶이기 때문에, 구분을 위해 가장 바깥쪽은 ""으로 묶어준다.
        sql_insert = "insert into dept2(deptno, dname, loc) values(91, '10강의실', '서울')"
        # 실행
        cursor.execute(sql_insert)

        # 현재 insert를 해 select로 확인 하였을때는 정상적으로 완료 되었다.
        # 그러나 실제 DB 서버에서는 변경 사항을 확인 할 수 없다.
        # 이유? 'COMMIT'을 해야만 한다.
        # DML(insert, update, delete)을 수행 후에는 반드시 'COMMIT'을 해야만,
        # 변경 사항이 영구적으로 DB에 적용된다.
        connection.commit()

        # 결과 확인 위한 select 문 실행 후, 출력
        sql_select = 'select * from dept2'
        cursor.execute(sql_select)
        for row in cursor:
            print(row)
            # (10, 'ACCOUNTING', 'NEW YORK')
            # ...
            # (22, 'ABC', 'KOREA')
            # (91, '10강의실', '서울') ~~~> insert 성공

