"""
항등 행렬(Indentity matrix): 대각선의 원소는 1이고, 나머지 원소는 0인 정사각행렬
    A @ I = I @ A = A를 만족
역행렬(Inverse matrix): A @ A- = A- @ A = I를 만족하는 행렬
전치 행렬(Transpose matrix): 행렬의 row와 column을 서로 바꾼 행렬

"""
import numpy as np

# numpy.c_ (column bind)와 numpy_r (row bind)의 비교
a = np.array([1, 2, 3])
print(a, type(a), a.shape)
b = np.array([4, 5, 6])
print(b, type(b), b.shape)

c = np.c_[a, b]
print(c, type(c), c.shape)

d = np.r_[a, b]
print(d, type(d), d.shape)

e = np.array([[1, 2, 3],
              [4, 5, 6]])
f = np.array([[10, 20],
              [30, 40]])
print(np.c_[e, f])  # e와 f의 row 개수가 같아야 column 방향으로 붙일 수 있음.
# print(np.r_[e, f])  # e와 f의 column 개수가 다르면 row 방향으로 붙일 수 없음!

g = np.array([[100, 200, 300]])
# print(np.c_[e, g])  # row의 개수가 다르기 때문에 오른쪽으로 붙일 수 없음!
print(np.r_[e, g])  # column의 개수가 같아야 밑으로 붙일 수 있음.

# (2, 3) shape의 모든 원소가 1인 array를 생성해서 출력: A
print(np.ones((2, 3), dtype=np.int))

# (2, 3) shape의 모든 원소가 0인 array를 생성해서 출력: B
print(np.zeros((2, 3), dtype=np.int))

# (3, 2) shape의 원소는 1 ~ 6인 array를 생성해서 출력: C
print(np.arange(1, 7).reshape((3, 2)))

# (3, 2) shape의 난수들로 이루어진 array를 생성해서 출력: D
print(np.random.random((3, 2)))

"""다음과 같은 결과가 나올 수 있도록 
numpy를 사용하지 않고 add(x, y), subtract(), multiply(), divide(), dot() 함수를 구현
|1 2| + |5 6|= |6  8 | 
|3 4|   |7 8|  |10 12|

|1 2| - |5 6|= |-4 -4| 
|3 4|   |7 8|  |-4 -4|

|1 2| * |5 6|= |5  12| 
|3 4|   |7 8|  |21 32|

|1 2| / |5 6|= |0.2   0.333| 
|3 4|   |7 8|  |0.428 0.5  |

|1 2| @ |5 6|= |19 22| 
|3 4|   |7 8|  |43 50|
위의 결과와 같은 결과를 주는 numpy 코드를 작성
"""

def add(x,y):
    result = []
    for i in range(len(x[0])):
        for j in range(len(x[1])):
            result.append(x[i][j] + y[i][j])
    result = np.array(result)
    result = result.reshape(len(x), len(x[0]))

    return result


def subtract(x, y):
    result = []
    for i in range(len(x)):
        for j in range(len(x[0])):
            result.append(x[i][j] - y[i][j])
    result = np.array(result)
    result = result.reshape(len(x), len(x[0]))

    return result


def multiply(x, y):
    result = []
    for i in range(len(x)):
        for j in range(len(x[0])):
            result.append(x[i][j] * y[i][j])
    result = np.array(result)
    result = result.reshape(len(x), len(x[0]))

    return result


def divide(x, y):
    result = []
    for i in range(len(x)):
        for j in range(len(x[0])):
            result.append(x[i][j] / y[i][j])
    result = np.array(result)
    result = result.reshape(len(x), len(x[0]))

    return result

def dot(x, y):
    """
    두 행렬 x와 y의 dot 연산 결과를 리턴.
        dot_ik = sum(j)[x_ij * y_jk]
    또한, dot 연산을 위해서는 행렬 x의 열(col)과 y의 행(row)의 개수가 같아야 한다.
    """
    print('x shape :', x.shape)
    print('y shape :', y.shape)
    if x.shape[1] != y.shape[0]:
        raise ValueError('행렬 x의 열(col)과 y의 행(row)의 개수가 같아야 합니다.')

    n_row = x.shape[0] # 행렬 x의 col 개수 ~~~> result의 row 개수가 된다.
    n_col = y.shape[1] # 행렬 y의 row 개수 ~~~> result의 col 개수가 된다.
    temp = x.shape[1] # 각 원소들끼리 곱한 결과를 더하는 횟수는 행렬 x의 열(col) 개수가 될 것.
    result = [] # 결과를 저장할 리스트

    for i in range(n_row): # 행렬 x의 row 개수만큼 반복
        for k in range(n_col): # 행렬 y의 col 개수만큼 반복
            n = 0 # dot 결과 행렬의 [i, k]번째 원소의 값을 계산
            for j in range(temp):
                n += x[i, j] * y[j, k]
            result.append(n) # 계산된 [i, k]번쨰 원소를 결과 리스트에 추가
    result = np.array(result)
    result = result.reshape(n_row, n_col) # result 리스트를 array로 변환하고, (n_row x n_col) 모양으로 변환

    return result


if __name__ == '__main__':
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])

    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))
    print(dot(x, y))



