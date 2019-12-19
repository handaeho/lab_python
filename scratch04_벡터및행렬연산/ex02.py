"""
numpy 패키지를 사용한 벡터 연산
"""
import math
import numpy as np

print('numpy version : ', np.__version__) # numpy version :  1.17.4

# 두 벡터의 덧셈
v = [1, 2] # ~~~> class list
print('v = ', v)

w = [2, 3]
print('w = ', w)

print(v + w) # [1, 2, 2, 3]
# print(v - w) ~~~> 리스트 간의 '-'는 에러 발생.

v.extend(w)
print(v) # [1, 2, 2, 3]
# 'v + w'는 v와 w는 그대로 유지한 채, v, w를 합친 새로운 리스트를 리턴한다.
# 'v.extend()'는 v에 w를 붙여서 v를 바꾼다.

# numpy 패키지의 ndarray 타입 사용
v1 = np.array([1, 2])
print(type(v1)) # <class 'numpy.ndarray'>
print(v1) # [1 2]
print('dimension = ', v1.ndim) # dimension =  1 ~~~> v1는 1차원 배열

v2 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(type(v2)) # <class 'numpy.ndarray'>
print(v2)
print('dimension = ', v2.ndim) # dimension =  2 ~~~> v2는 2차원 배열

# 배열 1개는 1차원 배열, 배열 안에 배열이 있으면 2차원, 배열 안에 배열안에 배열이 있으면 3차원 배열, ...

vv = np.array([
    1,
    [1, 2],
    [3, 4]
])
print(vv) # [1 list([1, 2]) list([3, 4])]
print('dimension = ', vv.ndim) # dimension =  1 ~~~> 이런 형태의 vv는 1차원 배열이다.

# 배열의 차원이 높아지려면, 배열 안의 모든 원소가 배열이어야 한다.

print('shape = ', v1.shape) # shape =  (2,) ~~~> 1차원 배열(v1)의 모양(원소 개수, )
print('shape = ', v2.shape) # shape =  (3, 2) ~~~> 2차원 배열(v2)의 모양(행, 열)
print('shape = ', vv.shape) # shape =  (3,) ~~~> 1차원 배열(vv)의 모양(원소 개수, )

# ndarray 타입을 사용한 벡터 연산
v = np.array([1, 2, 3])
w = np.array([3, 4, 5])

vector_add = v + w
print(vector_add) # [4 6 8]
# 두 벡터간의 원소 개수가 다르면 연산을 할 수 없다.
# (ValueError: operands could not be broadcast together with shapes (2,) (3,) )

vector_sub = v - w
print(vector_sub) # [-2 -2 -2]

# 2차원 배열 생성
vectors = np.array([
    [1, 2],
    [3, 4]
])
np_sum = np.sum(vectors) # 2차원 배열의 모든 원소들의 합
print('np_sum = ', np_sum) # np_sum =  10

# axis = 축 ~~~> axis=0은 column, axis=1은 row
np_sum_by_col = np.sum(vectors, axis=0) # 2차원 배열의 열 끼리의 합
print('np_sum_by_col = ', np_sum_by_col) # np_sum_by_col =  [4 6]

np_sum_by_row = np.sum(vectors, axis=1)
print('np_sum_by_row = ', np_sum_by_row) # np_sum_by_row =  [3 7]

np_mean = np.mean(vectors)
print('np_mean = ', np_mean) # 2차원 배열의 모든 원소들의 평균

np_mean_by_col = np.mean(vectors, axis=0) # 2차원 배열의 열의 평균
print('np_mean_by_col = ', np_mean_by_col) # np_mean_by_col =  [2. 3.]

np_mean_by_row = np.mean(vectors, axis=1) # 2차원 배열의 행의 평균
print('np_mean_by_row = ', np_mean_by_row) # np_mean_by_row =  [1.5 3.5]

# 스칼라 곱
v = np.array([1, 2, 3])
scalar_mult = v * 3
print('scalar_mult = ', scalar_mult) # scalar_mult =  [3 6 9]

# 물론 나누기도 가능하다.
v = np.array([1, 2, 3])
scalar_div = v / 3
print('scalar_div = ', scalar_div) # scalar_div =  [0.33333333 0.66666667 1.        ]
# 단, 나누기는 연산 식 위치를 잘 확인 해야한다. 결과가 달라진다.
scalar_div2 = 3/ v
print('scalar_div2 = ', scalar_div2) # scalar_div2 =  [3.  1.5 1. ]

# 내적(Dot Product) ~~~> 벡터의 성분 별로 곱한 후, 합
v = np.array([1, 2])
w = np.array([3, 4])
print('dot = ', v.dot(w)) # dot = 11 (= (1x3) + (2x4))

# numpy를 사용해, 벡터의 크기 계산(= sqrt(자신의 내적)
def norm(v):
    return math.sqrt(v.dot(v))

v = np.array([1, 1])
print('norm = ', norm(v)) # norm =  1.4142135623730951

# numpy를 사용해, 두 벡터 사이의 거리 계산
def dist(v, w):
    return norm(v - w) # 벡터 v에서 벡터 w를 빼서, 그 벡터의 크기를 구하면 거리가 될 것.

v = np.array([1, 2])
w = np.array([3, 4])
print('dist = ', dist(v, w)) # dist =  2.8284271247461903



