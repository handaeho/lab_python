import cx_Oracle
import pandas as pd


def get_column_names_of(table, cursor):
    # sql = f"""select column_name from user_tab_columns
    #      where table_name = '{table.upper()}'
    #      order by column_id"""
    # cursor.execute(sql)
    sql = """select column_name from user_tab_columns
    where table_name = :tbl_name
    order by column_id"""
    cursor.execute(sql, tbl_name=table.upper())  # data binding
    # cursor가 sql 문장의 :변수 위치에 데이터 타입에 맞게끔 값을 치환해 줌.
    # 값이 문자열이면 '문자열' 형태로 :변수 위치에 치환됨.
    col_names = [row[0] for row in cursor]
    return col_names


def select_all_from(table, cursor):
    sql = f'select * from {table.upper()}'
    # from 구문에서 테이블 이름은 ''로 감싸면 안되기 때문에
    # data binding 방식을 사용할 수 없다.
    cursor.execute(sql)
    # data = cursor.fetchall()  # [row for row in cursor]
    data_frame = pd.DataFrame(cursor)  # pd.DataFrame(data)
    # 데이터 프레임에 컬럼 이름을 설정
    data_frame.columns = get_column_names_of(table, cursor)
    return data_frame


if __name__ == '__main__':
    # 오라클 DB 서버에 접속
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        # Cursor 객체 생성
        with connection.cursor() as cursor:
            emp_columns = get_column_names_of('emp', cursor)
            print(emp_columns)  # ['empno', 'enam', 'job', ...]

            emp_df = select_all_from('emp', cursor)  # pandas.DataFrame
            # DataFrame은 테이블의 컬럼 이름(인덱스)를 포함하고 있어야 함.
            print(emp_df)

            dept_df = select_all_from('DEPT', cursor)
            print(dept_df)

            salgrade_df = select_all_from('salgrade', cursor)
            print(salgrade_df)

            # DataFrame에 새로운 컬럼을 추가 ~~~> DataFrame['컬럼 이름'] = List, pandas.Series
            # emp_df에 salgrade 컬럼을 추가
            # emp_df['sal'] 개수만큼 대해서 반복:
            sal_grade = [] # 급여 등급을 저장할 List
            for sal in emp_df['SAL']:
                # 선택된 sal 값이 salgrade_df 어느 grade에 속하는 지를 찾음
                # -> salgrade_df의 행 개수만큼 반복하면서 LO, HI와 비교
                # -> DataFrame.iterrows() 함수 :  데이터프레임의 (행 이름, 행) 튜플을 반복문 안에서 사용할 수 있게 함.
                for row_name, row in salgrade_df.iterrows(): # ~> row_name에 행 이름을, row에 행을 넣어 튜플을 분해한다.
                    if row['LOSAL'] <= sal <= row['HISAL']:
                        sal_grade.append(row['GRADE']) # 해당하는 급여의 등급을 찾은 경우 리스트에 append.
                        break # 찾았으니까 반복문 종료
            emp_df['SALGRADE'] = sal_grade # 데이터프레임에 'SALGRADE'라는 새로운 컬럼 추가
            print(emp_df)

            # SQL Join ~~~> pandas.merge()
            emp_dept = pd.merge(emp_df, dept_df, how='inner', on='DEPTNO')
            # ~> 'emp_df'와 'dept_df'를 'DEPTNO' 기준으로 'inner join' 하겠다.
            print(emp_dept)

            # join의 기준이 되는 컬럼이름이 데이터프레임마다 다르다면? ~~~> left / right join
            # left_on='left 데이터 프레임 컬럼' / right_on='right 데이터프 레임 컬럼'
            emp_dept_left = pd.merge(emp_df, dept_df, how='left', on='DEPTNO')
            emp_dept_right = pd.merge(emp_df, dept_df, how='right', on='DEPTNO')
            print(emp_dept_left)
            # ...
            # 13   7934  MILLER      CLERK  7782.0  ...     10         2  ACCOUNTING  NEW YORK
            # [14 rows x 11 columns]
            print(emp_dept_right)
            # ...
            # 14     NaN     NaN        NaN     NaN  ...     40       NaN  OPERATIONS    BOSTON
            # [15 rows x 11 columns]

            #  emp 테이블에서 mgr과 empno가 일치하는 join
            # 1) inner 2) left 3) right
            emp_mgr_empno_inner = pd.merge(emp_df, emp_df, how='inner', left_on='MGR', right_on='EMPNO')
            emp_mgr_empno_left = pd.merge(emp_df, emp_df, how='left', left_on='MGR', right_on='EMPNO')
            emp_mgr_empno_right = pd.merge(emp_df, emp_df, how='right', left_on='MGR', right_on='EMPNO')
            print(emp_mgr_empno_inner)
            print(emp_mgr_empno_left)
            print(emp_dept_right)
            print(emp_mgr_empno_right[['EMPNO_x', 'ENAME_x', 'MGR_x', 'EMPNO_y', 'ENAME_y']])


