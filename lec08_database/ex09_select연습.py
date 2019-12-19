"""
select 연습
1) emp 테이블에서 부서 번호를 입력받아, 해당 부서 직원들의 사번, 이름, 부서 번호를 출력
2) emp 테이블에서 사원 이름의 일부를 입력받아, 해당 글자가 포함된 직원들의 사번, 이름, 급여를 출력
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        # 1)
        deptno = input('부서 번호? >>> ')

        sql_ex1 = 'select empno, ename, deptno from emp where deptno = :deptno'
        cursor.execute(sql_ex1, deptno=deptno)
        for row in cursor:
            print(row)

        print('==================================')

        # 2)
        ename_s = input('사원 이름?(한글자 이상) >>> ').upper()
        sql_ex2 = 'select empno, ename, sal from emp where ename like :ename_s'
        cursor.execute(sql_ex2, ename_s= '%'+ ename_s +'%')
        for row in cursor:
            print(row)

# 1, 2번을 이렇게 할 수도 있다.
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        sql1 = '''select empno, ename, deptno
        from emp where deptno = :deptno
        '''
        dept_no = int(input('부서 번호 입력>> '))
        cursor.execute(sql1, deptno=dept_no)
        for empno, ename, deptno in cursor:  # 성분 분해, unpacking
            print(empno, ename, deptno)

        print('==================================')

        sql2 = '''select empno, ename, sal
        from emp 
        where lower(ename) like :keyword 
        '''
        name = input('검색할 이름 입력>> ')
        name = name.lower()  # 입력한 문자열을 소문자로 변환
        name = '%' + name + '%'  # like 검색
        cursor.execute(sql2, keyword=name)
        for empno, ename, sal in cursor:
            print(empno, ename, sal)


