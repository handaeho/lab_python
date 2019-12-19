"""
Pandas groupby, aggregate, apply
"""
import pandas as pd
import numpy as np

np.random.seed(1234)

df = pd.DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': np.random.randint(0, 10, 5),
    'data2': np.random.randint(0, 10, 5)
})
print(df)
#   key1 key2  data1  data2
# 0    a  one      3      9
# 1    a  two      6      1
# 2    b  one      5      7
# 3    b  two      4      9
# 4    a  one      8      6

# groupby()
grouped1 = df.groupby('key1')
print(grouped1) # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001339C6C9B88>
# DataFrameGroupBy object ~~~> 그룹 연산을 적용 하기 위해 만든 임시 객체
# 그룹 연산 : count, sum, mean, median, va, std, min, max, ...

cnt = grouped1['data1'].count()
print(type(cnt)) # <class 'pandas.core.series.Series'>
print(cnt)
# key1
# a    3
# b    2
# Name: data1, dtype: int64
# ~~~> 위에서 'key1'을 기준으로 groupby했고, a가 3개고, b가 2개다.
print(cnt['a'], cnt['b']) # 3 2

print(grouped1['data1'].mean())
# key1
# a    5.666667
# b    4.500000
# Name: data1, dtype: float64

print(grouped1.mean())
#          data1     data2
# key1
# a     5.666667  5.333333
# b     4.500000  8.000000
print(grouped1['data1', 'data2'].mean())
#          data1     data2
# key1
# a     5.666667  5.333333
# b     4.500000  8.000000
# ~~~> 2개의 결과는 같다. pandas는 '숫자 컬럼'을 찾아서 평균을 계산 해준다.

grouped2 = df.groupby(['key2'])
print(grouped2.mean())

# groupby의 기준(by)이 2개 이상의 컬럼일 경우, '리스트를 전달'하면 된다.
grouped3 = df.groupby(['key1', 'key2'])
print(grouped3['data1'].count())
# key1  key2
# a     one     2
#       two     1
# b     one     1
#       two     1
# Name: data1, dtype: int64
# ~~~> 'key1 a'는 'key2 one'을 2개, 'key2 two'를 1개 갖고. 'key1 b'는 'key2 one'을 1개, 'key2 two'를 1개 갖는다.
# 즉, a이면서 one인 것은 2개, a이면서 two인 것은 1개, b이면서 one인 것은 1개, b이면서 two인 것은 1개.

print(grouped3.count())
#            data1  data2
# key1 key2
# a    one       2      2
#      two       1      1
# b    one       1      1
#      two       1      1

print(grouped3.mean())
#            data1  data2
# key1 key2
# a    one     5.5    7.5
#      two     6.0    1.0
# b    one     5.0    7.0
#      two     4.0    9.0

people = pd.DataFrame(np.random.randint(0, 10, (5, 5)),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jimmy', 'Travis'])
print(people)
#         a  b  c  d  e
# Joe     8  0  5  0  9
# Steve   6  2  0  5  2
# Wes     6  3  7  0  9
# Jimmy   0  3  2  3  1
# Travis  3  1  3  7  1

print(people.groupby(len).sum()) # ~~~> 인덱스(이름) 길이로 groupby하고 해당 값들 sum
#     a  b   c  d   e
# 3  14  3  12  0  18
# 5   6  5   2  8   3
# 6   3  1   3  7   1


print(people.groupby(lambda x: x.startswith('J')).sum()) # ~~~> 문자열이 'J'로 시작하면 True, 아니라면 False
#         a  b   c   d   e
# False  15  6  10  12  12 ---> Steve, Wes, Travis의 각 값들의 합
# True    8  3   7   3  10 ---> Joe와 Jimmy의 각 값들의 합




