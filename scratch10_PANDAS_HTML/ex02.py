import pandas as pd
import cx_Oracle

from scratch09_CSV파일_SQL쿼리.ex10 import select_all_from

def peak_to_peak(x):
    return x.max() - x.min()


if __name__ == '__main__':
    # Oracle DB Server connection
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:

    # cursor 객체 생성
        cursor = connection.cursor()

    # scratc09.ex10에서 작성한 테이블 전체 검색 패키지 함수 사용해서 emp_df 생성
        emp_df = select_all_from('emp', cursor)

    # emp_df를 csv 파일로 저장
        emp_df.to_csv('emp_df.csv', index=False)

    # emp_df를 부서별로 그룹화
        dept = emp_df.groupby('DEPTNO')

    # emp_df에서 부서별 평균 급여
        dept_sal_mean = dept['SAL'].mean()
        print(dept_sal_mean)
        print(' ===================================================================================== ')

    # emp_df에서 부서별 인원 수
        dept_people_cnt = dept['EMPNO'].count()
        print(dept_people_cnt)
        print(' \n ===================================================================================== ')

    # emp_df에서 부서별 최소 급여
        dept_min_sal = dept['SAL'].min()
        print(dept_min_sal)
        print(' \n ===================================================================================== ')

    # emp_df에서 부서별 최대 급여
        dept_max_sal = dept['SAL'].max()
        print(dept_max_sal)
        print(' \n ===================================================================================== ')

    # 위의 결과들을 하나의 DataFrame으로 출력
        df = pd.DataFrame({
            'dept_sal_mean': dept_sal_mean,
            'dept_people_cnt': dept_people_cnt,
            'dept_min_sal': dept_min_sal,
            'dept_max_sal': dept_max_sal
        })
        print(df)
        print(' \n ===================================================================================== ')

    # emp_df에서 직책별 인원 수와 평균/최소/최대 급여
        job = emp_df.groupby('JOB')
        job_people_cnt = job['EMPNO'].count()
        job_sal_mean = job['SAL'].mean()
        job_min_sal = job['SAL'].min()
        job_max_sal = job['SAL'].max()

        print(job_people_cnt, job_sal_mean, job_min_sal, job_max_sal)
        print(' \n ===================================================================================== ')

    # emp_df에서 부서별, 직책별 인원 수, 평균/최소/최대 급여
        dept_job = emp_df.groupby(['DEPTNO', 'JOB'])
        dept_job_people_cnt = dept_job['EMPNO'].count()
        dept_job_sal_mean = dept_job['SAL'].mean()
        dept_job_min_sal = dept_job['SAL'].min()
        dept_job_max_sal = dept_job['SAL'].max()

        print(dept_job_people_cnt, dept_job_sal_mean, dept_job_min_sal, dept_job_max_sal)

        # agg()를 사용하면
        grouped = emp_df.groupby(['DEPTNO', 'JOB'])
        sal_by_dept_job = grouped['SAL']
        df2 = sal_by_dept_job.agg({
            'count': 'count',
            'mean': 'mean',
            'min': 'min',
            'max': 'max',
            'range': lambda x: x.max() - x.min()
        })
        print(df2)
        # agg() 함수의 파라미터에 dict를 전달하는 방식은 pandas 패키지가 업그레이드 되면 없어질수도 있어서,
        # FutureWarning 메세지가 나온다.
        # 따라서, dict 방식 보다는 keyword-argument 방식이 권장된다.
    print(' \n ===================================================================================== ')

    # aggregate() ~~~> 여러개의 함수를 적용할 수 있다.
    df2 = dept['SAL'].agg(['count', 'mean', 'min', 'max'])
    # aggregate() 함수의 파라미터에 '함수 이름'을 전달하면, groupby 객체에 함수를 적용.
    # 전달하려는 함수가 '집계 함수'라면, 전달하려는 함수 이름을 '문자열'로 전달.
    # 집계 함수 : Series Ehsms DataFrame 클래스가 가지고 있는 메소드들 -> count, mean, min, max, ...
    print(df2)

    # 직접 작성한 함수를 전달하려면 '함수 이름'을 전달한다.(문자열 X)
    df3 = dept['SAL'].agg(peak_to_peak)
    print(df3)
    # agg()에는 'lambda' 역시 사용 가능하다
    df4 = dept['SAL'].agg(lambda x: x.max() - x.min())
    print(df4)

    # agg() 함수가 만드는 DataFrame의 컬럼 이름을 설정 할 때는
    # keyword Argument 방식 또는 dict를 파라미터로 전달.
    print(dept['SAL'].agg(count='count',  avg='mean', max='max', min='min', ange=lambda x: x.max() - x.min()))


