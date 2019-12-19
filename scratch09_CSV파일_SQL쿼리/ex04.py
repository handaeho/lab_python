"""
pandas 모듈을 사용해 csv 파일 처리
"""
import pandas as pd
import os
import matplotlib.pyplot as plt

file_path = os.path.join('..', 'scratch08_경사하강법', 'mpg.csv')

df = pd.read_csv(file_path)

print(df.head()) # ~> head(n) : 0 ~ n행 출력. defalut n = 5
#    Unnamed: 0 manufacturer model  displ  year  ...  drv cty hwy  fl    class
# 0           1         audi    a4    1.8  1999  ...    f  18  29   p  compact
# 1           2         audi    a4    1.8  1999  ...    f  21  29   p  compact
# 2           3         audi    a4    2.0  2008  ...    f  20  31   p  compact
# 3           4         audi    a4    2.0  2008  ...    f  21  30   p  compact
# 4           5         audi    a4    2.8  1999  ...    f  16  26   p  compact

print('shape : ', df.shape) # shape : (행 개수, 열 개수(변수 개수))
# shape :  (234, 12)

print('type : ', df.dtypes) # dtype : 각 컬럼(변수)의 타입
# type :  Unnamed: 0        int64
# manufacturer     object
# model            object
# displ           float64
#...
# hwy               int64
# fl               object
# class            object
# dtype: object
# ~~~> object(문자열), float(실수), int(정수)

print(df.describe()) # 숫자형 변수들의 기술 요약 통계량
#        Unnamed: 0       displ         year         cyl         cty         hwy
# count  234.000000  234.000000   234.000000  234.000000  234.000000  234.000000
# mean   117.500000    3.471795  2003.500000    5.888889   16.858974   23.440171
# std     67.694165    1.291959     4.509646    1.611534    4.255946    5.954643
# min      1.000000    1.600000  1999.000000    4.000000    9.000000   12.000000
# 25%     59.250000    2.400000  1999.000000    4.000000   14.000000   18.000000
# 50%    117.500000    3.300000  2003.500000    6.000000   17.000000   24.000000
# 75%    175.750000    4.600000  2008.000000    8.000000   19.000000   27.000000
# max    234.000000    7.000000  2008.000000    8.000000   35.000000   44.000000

# df['컬럼이름'] : 데이터 프레임에서 특정 컬럼의 모든 데이터를 선택
displ = df['displ']
print(displ)
# 0      1.8
# 1      1.8
# 2      2.0
# ...
# 232    2.8
# 233    3.6
# Name: displ, Length: 234, dtype: float64

cty = df['cty']
print(cty)
# 0      18
# 1      21
# 2      20
# ...
# 232    18
# 233    17
# Name: cty, Length: 234, dtype: int64

# 그래프 그리기
plt.scatter(displ, cty)
plt.show()

# 데이터 프레임에서 '행'을 추출하고자 할 때 ~~~> loc[행 레이블] / iloc[행 번호(인덱스)]
# 행 레이블이 없는 경우, 행의 인덱스로 자동으로 레이블을 설정한다.
print(df.loc[1])
print(df.iloc[1])
print(df.iloc[0:3]) # row index 0 이상 3 미만인 행 선택

# 데이터 프레임에서 여러개의 컬럼 선택
cols = ['displ', 'cty', 'hwy'] # [] ~> 리스트
print(df[cols]) # [] ~> 인덱스 연산자 <-------- 차이점을 꼭 기억하자.
# [3 rows x 12 columns]
#      displ  cty  hwy
# 0      1.8   18   29
# 1      1.8   21   29
# ...
# 233    3.6   17   26
# [234 rows x 3 columns]

# 데이터 프레임에서 여러개의 행(관측값)과 컬럼(변수) 선택
# df.loc[row_labels, col_labels] : 행과 열의 레이블(이름)
# df.iloc[row_index, col_index] : 행과 열의 인덱스
print(df.loc[0:3, cols]) # ~> 레이블이 0, 1, 2, 3인 행 출력(여기서는 레이블이 따로 없으므로 인덱스가 레이블이 됨)
# [234 rows x 3 columns]
#    displ  cty  hwy
# 0    1.8   18   29
# 1    1.8   21   29
# 2    2.0   20   31
# 3    2.0   21   30
print(df.iloc[0:3, 0:3]) # ~> 인덱스 0, 1, 2 행 출력
#    Unnamed: 0 manufacturer model
# 0           1         audi    a4
# 1           2         audi    a4
# 2           3         audi    a4

