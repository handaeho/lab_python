"""
1) ex08.py에서 만든 emp.csv 파일로 DataFrame 생성
2) 급여(sal)가 2000이상인 직원들의 모든 정보 출력
3) 부서번호(deptno)가 10번인 직원들의 모든 정보 출력
4) 급여가 전체 직원의 평균 이상인 직원들의 사번, 이름, 급여 출력
5) 30번 부서에서 일하는 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호 출력
6) 20번, 30번 부서에서 일하는 작원 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호 출력
7) 수당이 없는 직원 중, 매니저가 있고 직책이 MANAGER 또는 CLERK인 직원들의 모든정보 출력
8) 사원 이름에 'E'가 포함된 직원의 이름 출력(str.contains() 사용)
9) DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서 실행
"""
import pandas as pd

# 1) ex08.py에서 만든 emp.csv 파일로 DataFrame 생성
print(' 1번 ============================================================================')
emp = pd.read_csv('emp.csv', sep=',', encoding='utf-8',
                  names=['EMPNO', 'ENAME', 'JOB', 'MGR', 'HIREDATE', 'SAL', 'COMM', 'DEPTNO'])
print(emp[0:5])

# 2) 급여(sal)가 2000이상인 직원들의 모든 정보 출력
print(' \n 2번 ============================================================================')
print(emp[emp['SAL'] >= 2000])

# 3) 부서번호(deptno)가 10번인 직원들의 모든 정보 출력
print(' \n 3번 ============================================================================')
print(emp[emp['DEPTNO'] == 10])

# 4) 급여가 전체 직원의 평균 이상인 직원들의 사번, 이름, 급여 출력
print(' \n 4번 ============================================================================')
cond1 = (emp['SAL'] >= emp['SAL'].mean())
print(emp['SAL'].mean())
print(emp[cond1][['EMPNO', 'ENAME', 'SAL']])

# 5) 30번 부서에서 일하는 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호 출력
print(' \n 5번 ============================================================================')
cond2 = (emp['JOB'] == 'SALESMAN')
print(emp[cond2][['EMPNO', 'ENAME', 'SAL']])

# 6) 20번, 30번 부서에서 일하는 직원 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호 출력
print(' \n 6번 ============================================================================')
cond3 = emp['DEPTNO'] == 20
cond4 = emp['DEPTNO'] == 30
cond5 = emp['SAL'] > 2000
subset1 = emp[(cond3 | cond4) & cond5]
print(subset1[['EMPNO', 'ENAME', 'SAL']])

# 7) 수당이 없는 직원 중, 매니저가 있고 직책이 MANAGER 또는 CLERK인 직원들의 모든정보 출력
print(' \n 7번 ============================================================================')
c1 = emp['COMM'].isna()
c2 = ~emp['MGR'].isna() # ~ : not
c3 = emp['JOB'].isin(['MANAGER', 'CLERK'])

subset2 = emp[c1 & c2 & c3]
print(subset2)

# 8) 사원 이름에 'E'가 포함된 직원의 이름 출력(str.contains() 사용)
print(' \n 8번 ============================================================================')
name_all = pd.Series(emp['ENAME'])
name_in_e = name_all[name_all.str.contains('E')]
print(name_in_e)

# 9) DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서 실행
print(' \n 9번 ============================================================================')
emp.to_csv('emp_new.csv', index=False)