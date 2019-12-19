import pandas as pd

if __name__ == '__main__':
    # csv 파일에서 DataFrame 생성
    emp_df = pd.read_csv('emp_df.csv')
    print(emp_df.iloc[0:5])

    # 부서별, 직책별 직원 수를 출력
    grouped1 = emp_df.groupby(['DEPTNO', 'JOB'])
    emp_by_dept = grouped1['EMPNO']
    result_df = emp_by_dept.agg('count')
    print(result_df)

    # stack() : 위에서 아래로 쌓는다.
    # unstack() : 옆으로 늘어놓는다.
    print(result_df.unstack())

    # grouping 기준이 되는 컬럼의 값들이 index(행의 이름)로 사용되지 않고 컬럼으로 사용하려면
    # 파라미터 as_index = False 설정 (defalut는 True)
    grouped2 = emp_df.groupby('DEPTNO', as_index=False)
    emp_by_dept_2 = grouped2['EMPNO']
    result_df2 = emp_by_dept_2.agg('count')
    print(result_df2)

    grouped3 = emp_df.groupby(['DEPTNO', 'JOB'], as_index=False)
    emp_by_dept_3 = grouped3['EMPNO']
    result_df3 = emp_by_dept_3.agg('count')
    print(result_df3)

    