"""
Join
emp 테이블과 dept 테이블을 사용해,
부서 번호를 입력 받아 해당 부서 사원의 사번, 이름, 급여, 부서 번호, 부서 이름 출력
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        # 1) Oracle 방식
        dept_no = input('부서 번호? >>> ')
        sql_oracle = '''select e.empno, e.ename, e.sal, e.deptno, d.deptno 
                    from emp e , dept d  
                    where e.deptno = d.deptno and e.deptno = :deptno'''
        cursor.execute(sql_oracle, deptno=dept_no)
        for row in cursor:
            print(row)

        # 2) ANCI 표준 방식
        deptno = input('부서 번호? >>> ')
        sql_anci = '''select e.empno, e.ename, e.sal, e.deptno, d.deptno 
                            from emp e join dept d  
                            on e.deptno = d.deptno 
                            where e.deptno = :deptno'''
        cursor.execute(sql_anci, deptno=deptno)
        for row in cursor:
            print(row)

