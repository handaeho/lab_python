"""
numpy의 행렬 관련 함수
"""
import numpy as np

# numpy.ndarray 타입의 객체 생성
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(A)
print(B)

print(A.shape) # (2, 3) ~~~> 2행 3열
print(B.shape) # (3, 2) ~~~> 3행 2열

# 이렇게도 된다.
nrows, ncols = B.shape
print(nrows, 'X', ncols) # 3 X 2

# Slicing : 행렬에서 특정 행, 열을 뽑아냄
# 리스트에서는 list[row][col] / numpy에서는 ndarray[row, col]
print(A[0, 0]) # 1
print(A[0, 2]) # 3
print(A[0, 0:2]) # [1 2] ~~~> 0번째 행의 0 ~ 2열 까지
print(A[0:2, 0:2]) # [[1 2] [4 5]] ~~~> 0 ~ 2행의 0 ~ 2열
print(A[:, 0:2]) # 모든 행의 0 ~ 2열 <<콜론(:)은 생략 불가>>
print(A[0:2, :]) # 0 ~ 2행의 모든 열
print(A[:, 0]) # 인덱스 0번 col의 원소들로 이루어진 array
print(A[0, :]) # 인덱스 0번 row의 원소들로 이루어진 array
# 리스트에서는 이런 기능이 불가. numpy.ndarray에서는 가능

# 단위 행렬
identity_matrix = np.identity(3, dtype=int) # 3 X 3, int 타입 단위 행렬
print(identity_matrix)

# 전치 행렬
transpose_matrix = np.transpose(A) # = A.transpose()
print(transpose_matrix)

# 행렬 곱셈
print(A.dot(B)) # A 행렬 * B 행렬
print(B.dot(A)) # B 행렬 * A 행렬




