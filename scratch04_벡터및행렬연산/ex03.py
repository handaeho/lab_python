"""
2차원 리스트를 이용한 행렬
matrix ~~~> 행 / matrix[index] ~~~> 열
"""
def shape(matrix):
    """
    행렬의 행과 열의 개수를 tuple 형태로 리턴하는 함수

    :param matrix: n X m 행렬 (행의 개수가 n개, 열의 개수가 m개인 2차원 리스트)
    :return: tuple (n, m)
    """
    nrows = len(matrix)
    ncols = len(matrix[0])
    return nrows, ncols
    # 행(row)은 전체 2차원 리스트의 길이와 같고 (원소의 개수)
    # 열(col)은 2차원 리스트 그 각 안의 리스트 인덱스 수와 같으므로

def get_row(matrix, index):
    """
    주어진 행렬에서 index에 해당하는 row를 리턴하는 함수

    :param matrix: n X m 행렬
    :param index: 행 번호(0부터 시작)
    :return: vector(원소가 m개인 1차원 리스트)
    """
    return matrix[index]

def get_col(matrix, index):
    """
    주어진 행렬에서 index에 해당하는 column을 리턴하는 함수

    :param matrix: n X m 행렬
    :param index: 열 번호
    :return: vector(원소가 n개인 1차원 리스트)
    """
    # cols = []
    # for i in matrix:
    #     cols.append(i[index])
    #     i는 2차원 리스트 B 안에 있는 각 리스트([1, 2], [3, 4], [5, 6])를 반복하며,
    #     전달받은 index에 있는 값을 cols 리스트에 추가한다.
    # return cols

    # 위의 for문을 comprehension 하면,
    return [x[index] for x in matrix]

def make_martix(nrows, ncols, fn):
    """
    함수 fn의 리턴값들로 이루어진 nrows X ncols 행렬을 리턴하는 함수

    :param nrows: 행의 개수
    :param ncols: 열의 개수
    :param fn: 함수(fn(nrows, ncols) = 숫자)
    :return: nrows X ncols 행렬
    """
    # result = [] # 리스트를 원소로 갖는 2차원 리스트가 될 result 리스트
    # for i in range(nrows): # i가 전달받은 행의 수 만큼 반복하면서
    #     row = [] # 매번 row 리스트 생성. 행렬에 추가될 행이 되는 1차원 리스트
    #     for j in range(ncols): # j가 전달받은 열의 수만큼 반복하면서
    #         row.append(fn(i, j)) # row 리스트에 함수 fn을 수행한 결과를 추가
    #     result.append(row) # row 리스트를 result 리스트에 추가하고, 다시 처음부터 반복
    #     # 위에서 다시 row 리스트 생성하고, fn의 결과 값을 row에 추가하고, row를 result에 추가하고
    # return result

    # 이를 comprehension을 사용하면
    result = [[fn(i, j) for j in range(ncols)] for i in range(nrows)]
    return result
    # 먼저 열의 수(j)만큼 row 리스트를 생성하고, row 리스트의 원소로 fn의 결과값을 추가한 뒤,
    # 행의 수(i)만큼 row 리스트를 result 리스트에 추가해 리턴

def fn(x, y):
    return x + y

# 단위 행렬
def identity_matrix(x, y):
    result = 1 if x == y else 0 # 3항 연산자(항이 3개(result, x, y)인 연산자)
    return result
    # return 1 if x == y else 0 ~~~> 같은 의미!
    # 즉, lambda 표현식과 같다.

# 전치 행렬
def transpose_matrix(matrix):
    """
    n X m 행렬을 받아, m X n의 전치 행렬을 리턴하는 함수(행과 열을 뒤바꿈)
    :param matrix: n X m 행렬
    :return: m X n 행렬
    """
    trans_m = [] # 리스트를 원소로 가질 2차원 리스트

    for j in range(len(matrix[0])):
    # matrix[0] = matrix의 0번째 인덱스에 저장된 값 (A[0] = [1, 2, 3], A[1] = [4, 5, 6])
    # 즉, j를 열의 개수 만큼 반복한다.
        row =[]
        for i in matrix: # i를 행의 개수 만큼 반복한다.
           row.append(i[j]) # i번째 행의 j번째 인덱스에 저장된 값을 row 리스트에 추가
           # 예를 들어, 행렬 A에서 0[0] = 1, 1[0] = 4, 0[1] = 2, 1[1] = 5, 0[2] = 3, 1[2] = 6
        trans_m.append(row) # row 리스트를 trans_m 리스트에 추가해, 2차원 리스트로 생성

    return trans_m

def transpose_matrix_2(matrix):
# 또는 위에서 만든 'make_matrix' 메소드를 이용한다면
    nrows, ncols = shape(matrix)
    t = make_martix(ncols, nrows, lambda i, j: matrix[j][i]) # nrows를 ncols로, ncols을 nrows로 전달
    return t

def transpose_matrix_3(matrix):
# 아니면 'get_col' 메소드 이용하면
    nrows = len(matrix) # 원본 행렬의 행의 개수
    ncols = len(matrix[0])  # 원본 행렬의 열의 개수
    t = [] # 전치 행렬이 될 t

    for j in range(ncols): # 원본 행렬의 열 개수 만큼 반복
        t.append(get_col(matrix, j)) # 원본 행렬에서 j번째 열(col)을 꺼내서 t에 행(row)으로 추가

    return t

    # 이를 comprehension 하면
    # return [get_col(matrix, j) for j in range(ncols)]

def transpose_matrix_unpacking_zip(matrix):
    # unpacking과 zip() 함수를 이용한 전치 행렬
    t = []
    for col in zip(*matrix): # 행렬을 unpacking해, 각각의 tuple로 만들고, zip으로 꺼냄
        t.append(list(col)) # 하나의 열이 하나의 원소가 되어 t에 추가
        # 또한, 이때 t에 행렬의 열로 구성된 원소는 tuple로 추가 되기 때문에 list로 바꾸어 주어야 한다.
    return t

# 실행문
if __name__ == '__main__':
    # 2 X 3 행렬
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # 3 X 2 행렬
    B = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    print(shape(A)) # (2, 3)
    print(shape(B)) # (3, 2)

    print(get_row(A, 0)) # [1, 2, 3]
    print(get_col(B, 0)) # [1, 3, 5]

    print(make_martix(3, 3, fn)) # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    # 또는 fn을 호출 하지 않고 lambda 사용 시,
    print(make_martix(3, 3, lambda x, y: x + y)) # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    print(make_martix(2, 2, lambda x, y: x * y)) # [[0, 0], [0, 1]]

    print(make_martix(2, 2, identity_matrix)) # [[1, 0], [0, 1]] ~~~> 단위 행렬
    print(make_martix(2, 2, lambda x, y: 1 if x == y else 0))

    print(transpose_matrix(A)) # [[1, 4], [2, 5], [3, 6]] ~~~> 행렬 A의 전치 행렬
    print(transpose_matrix(B)) # [[1, 3, 5], [2, 4, 6]]

    print(transpose_matrix_2(A)) # [[1, 4], [2, 5], [3, 6]]
    print(transpose_matrix_2(B)) # [[1, 3, 5], [2, 4, 6]]

    print(transpose_matrix_3(A)) # [[1, 4], [2, 5], [3, 6]]
    print(transpose_matrix_3(B)) # [[1, 3, 5], [2, 4, 6]]

    # zip() 함수를 이용한 전치 행렬
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    for x, y, z in zip(a, b, c):
        # a에서 첫번째 꺼내 x에, b에서 첫번째 꺼내 y에, c에서 첫번째 꺼내 z에
        # a에서 두번째 꺼내 x에, b에서 두번째 꺼내 y에, c에서 두번째 꺼내 z에
        # a에서 세번째 꺼내 x에, b에서 세번째 꺼내 y에, c에서 세번째 꺼내 z에
        print(x, y, z)
        # 1 4 7
        # 2 5 8
        # 3 6 9 ~~~> 전치 행렬 완성

    # unpacking 연산자 : *
    print('A = ', A) # A =  [[1, 2, 3], [4, 5, 6]]
    print('*A = ', *A) # *A =  [1, 2, 3] [4, 5, 6]
    # 리스트 A를 unpacking.

    print('B = ', B)  # B =  [[1, 2], [3, 4], [5, 6]]
    print('*B = ', *B)  # *B =  [1, 2] [3, 4] [5, 6]
    # 리스트 B를 unpacking.

    print(transpose_matrix_unpacking_zip(A)) # [[1, 4], [2, 5], [3, 6]]
    print(transpose_matrix_unpacking_zip(B)) # [[1, 3, 5], [2, 4, 6]]

