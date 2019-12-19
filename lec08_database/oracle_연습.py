"""
oracle의 여러 SQL문을 연습해 보자
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        # 평균 급여보다 많이 받는 사원 정보 출력
        sql_mean_sal = 'select * from emp where sal > (select avg(sal) from emp)'
        cursor.execute(sql_mean_sal)
        for row in cursor:
            print(row)
            # (7566, 'JONES', 'MANAGER', 7839, datetime.datetime(1981, 4, 2, 0, 0), 2975.0, None, 20)
            # (7698, 'BLAKE', 'MANAGER', 7839, datetime.datetime(1981, 5, 1, 0, 0), 2850.0, None, 30)
            # (7782, 'CLARK', 'MANAGER', 7839, datetime.datetime(1981, 6, 9, 0, 0), 2450.0, None, 10)
            # ...

        print('=================================================')

        # 부서별 평균 급여
        sql_mean_dept = 'select deptno, avg(sal) from emp group by deptno'
        cursor.execute(sql_mean_dept)
        for row in cursor:
            print(row)
            # (30, 1566.6666666666667)
            # (20, 2175)
            # (10, 2916.6666666666665)

        print('=================================================')

        # 급여가 1000 이상인 사원들의 부서별 평균 급여를 출력.(단, 부서별 평균 급여가 2000 이상인 부서만)
        sql_1000 = 'select deptno, avg(sal) ' \
                   'from emp where sal >= 1000 ' \
                   'group by deptno ' \
                   'having avg(sal) >= 2000'
        cursor.execute(sql_1000)
        for row in cursor:
            print(row)
            # (20, 2518.75)
            # (10, 2916.6666666666665)

        print('=================================================')

        # 각 부서별 같은 업무(job)를 하는 사람의 인원수를 구해서
        # 부서번호, 업무(job), 인원수를 부서번호에 대해서 오름차순 정렬해서 출력.
        sql_job = '''select deptno, job, count(*) 
                     from emp 
                     group by deptno, job
                     order by deptno asc'''
        cursor.execute(sql_job)
        for row in cursor:
            print(row)

        print('=================================================')

        # 'DALLAS' 에서 근무하는 사원의 이름, 부서번호를 출력
        sql_dal = '''
        select ename, deptno
        from emp
        where deptno = (select deptno
                        from dept
                        where loc = :loc)'''
        cursor.execute(sql_dal, loc='DALLAS')
        for row in cursor:
            print(row)

        print('=================================================')

        # 평균 급여보다 낮은 직원을 찾아, 연봉 10% 인상 후, 출력
        sql_10 = '''
        select empno, ename, sal*1.1 
        from emp2 
        where sal < (select avg(sal) 
                     from emp2)'''
        cursor.execute(sql_10)
        for row in cursor:
            print(row)

        print('******************')

        # 이걸 update까지 하면
        sql_10_update = '''
        update into emp2 
        set sal = sal*1.1 
        where sal < (select avg(sal) from emp2)'''
        connection.commit()
        cursor.execute(sql_10)
        for row in cursor:
            print(row)