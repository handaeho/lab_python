"""
Pandas Package의 데이터 타입

- Series : 1차원 리스트. 인덱스가 1개.
- DataFrame : 2차원 리스트. 인덱스가 2개(행/열).

'Series 타입'은 출력하면 바로 '컬럼 이름 없이 데이터'가 나오고,
'DataFrame 타입'은 출력하면 '컬럼 이름이 나오고, 데이터'가 나온다.

"""
import pandas as pd
import numpy as np

a = pd.Series([1, 3, 5, np.nan, 6, 8])
print(type(a)) # <class 'pandas.core.series.Series'>
print(a)
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

print(a[0]) # Series에서 특정 인덱스 아이템 선택 : Series[index]. a[0]의 데이터 타입 : float
print(a[0:3]) # 인덱스 연산자([]) 안에서 범위 연산자(:)를 사용 가능. a[0:3]의 데이터 타입 : Series
print(a[[0, 2, 4]]) # 바깥쪽 [] ~> 인덱스 연산자 / 안쪽 [] ~> 리스트

b = pd.DataFrame([1, 3, 5, np.nan, 6, 8])
print(type(b)) # <class 'pandas.core.frame.DataFrame'>
print(b)
#      0 ~~~> 컬럼이름(지금은 따로 없어서 0)
# 0  1.0
# 1  3.0
# 2  5.0
# 3  NaN
# 4  6.0
# 5  8.0

# dict 타입({key : value, key : value, ...})의 데이터에서 DataFrame 생성
df = pd.DataFrame({
    'no': [3, 13, 23],
    'name': ['김영광', '이은지', '조유경'],
    'gender': ['M', 'F', 'F']
})
print(df)
#    no name gender
# 0   3  김영광      M
# 1  13  이은지      F
# 2  23  조유경      F

# 2차원 리스트 타입([[], [], [], ...]의 데이터에서 DataFrame 생성
student = pd.DataFrame([
    [4, '김재성', 'M'],
    [14, '이재경', 'M'],
    [24, '조지원', 'F']
])
print(student)
#     0    1  2
# 0   4  김재성  M
# 1  14  이재경  M
# 2  24  조지원  F

# 컬럼이름 부여하는 2가지 방법
student = pd.DataFrame([
    [4, '김재성', 'M'],
    [14, '이재경', 'M'],
    [24, '조지원', 'F']
], columns = ['번호', '이름', '성별'])
print(student)
# 또는
student.columns = ['번호', '이름', '성별'] # dataframe.columns : 리스트에 컬럼 이름 부여
print(student)
#    번호   이름 성별
# 0   4  김재성  M
# 1  14  이재경  M
# 2  24  조지원  F

# DataFrame.iloc[row index, col index]
print(student.iloc[0, 0]) # [0번 row, 0번 col]의 아이템 출력
print(student.iloc[0, 0:3]) # [0번 row, 0 ~ 2번 col]의 아이템 출력

print(type(student.iloc[0, 0:3])) # Series 타입
print(student.iloc[0:2, 0:2])
print(type(student.iloc[0:2, 0:2])) # DataFrame 타입

print(student.iloc[:, 1:3]) # 범위 연산자(:)만 사용하면, 모든 행 또는 열
print(student.iloc[1:3, :])
print(student.iloc[1:3]) # 모든 컬럼을 출력한다면, 컬럼 index는 생략 가능
print(student.iloc[:, 1:3]) # 단, 모든 행을 출력할하려고 생략 시, row index는 ':,'는 넣어 주어야 함

# Boolean Indexing
# dataframe[[boolean 리스트]] : 데이터 프레임에서 행 번호와 boolean 리스트를 매칭시켜서, True가 되는 인덱스를 선택한다.
print(student[[False, True, False]])
#    번호   이름 성별
# 1  14  이재경  M ~~~> 그래서 여기서 1번 인덱스를 갖는 행이 출력되는 것.

# 조건식을 이용 할 수도 있다.
condition = (student['성별'] == 'M')
print(condition)
# 0     True
# 1     True
# 2    False

print(student[condition]) # ~> student['성별'] == 'M'에 TRUE가 되는 row들을 출력하겠다.
#    번호   이름 성별
# 0   4  김재성  M
# 1  14  이재경  M

# 데이터 프레임 이어 붙이기 : concat
# pd.concat(['데이터프레임1', '데이터프레임2', ...])
student.columns = ['no', 'name', 'gender']
stu_df = pd.concat([df, student])
print(stu_df)
#    no name gender
# 0   3  김영광      M
# 1  13  이은지      F
# 2  23  조유경      F
# 0   4  김재성      M
# 1  14  이재경      M
# 2  24  조지원      F
# ~~~> 인덱스가 아닌 레이블을 사용해서 2개의 데이터 프레임을 붙인다.

print(stu_df.iloc[0])
# no          3
# name      김영광
# gender      M
print(stu_df.loc[0])
#    no name gender
# 0   3  김영광      M
# 0   4  김재성      M
# ~~~> 그래서 이렇게 iloc와 loc의 결과가 다르다.

stu_df2 = pd.concat([df, student], ignore_index=True)
print(stu_df2)
#    no name gender
# 0   3  김영광      M
# 1  13  이은지      F
# 2  23  조유경      F
# 3   4  김재성      M
# 4  14  이재경      M
# 5  24  조지원      F
# ~~~> 'ignore_index=True' 파라미터를 설정했더니, 레이블을 붙이지 않고, 재 인덱싱을 한다.

# 데이터 프레임을 concat하고 정렬하자 : sort_values('정렬 기준 컬럼이름')
print(stu_df2.sort_values('no'))
#    no name gender
# 0   3  김영광      M
# 3   4  김재성      M
# 1  13  이은지      F
# 4  14  이재경      M
# 2  23  조유경      F
# 5  24  조지원      F

# 데이터 프레임에서 여러개의 조건을 주고 검색
cond1 = stu_df2['no'] % 2 == 1 # no 컬럼의 값이 홀수
print(cond1)
# 0     True
# 1     True
# 2     True
# 3    False
# 4    False
# 5    False
cond2 = stu_df2['gender'] == 'F' # gender 컬럼의 값이 F
print(cond2)
# 0    False
# 1     True
# 2     True
# 3    False
# 4    False
# 5     True
subset = stu_df2[cond1 & cond2]
print(subset)
#    no name gender
# 1  13  이은지    F
# 2  23  조유경    F
# ~~~> cond1과 cond2가 모두 TRUE인 row 출력
# 이때 'and / or' 가 아닌 '& / |'를 사용해야 한다. (각 성분 별로 연산을 해야하기 떄문)

