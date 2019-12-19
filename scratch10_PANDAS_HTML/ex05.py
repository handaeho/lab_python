
"""
apply() 함수

aggregate 함수는 집계 함수들(count, sum, mean, std, ...)만 사용 가능
apply 함수는 집계 함수 이외의 함수들도 사용 가능

집계 함수는 '숫자 타입'의 컬럼만 자동으로 선택.
apply() 함수는 모든 컬럼 또는 행을 함수의 파라미터로 전달하기 때문에, 집계 함수는 제대로 동작하지 않을수도 있음.
"""
import pandas as pd
import numpy as np

def squares(x):
    return x ** 2


def doubles(x):
    return x * 2


if __name__ == '__main__':
    result1, result2 = squares(3), doubles(3)
    print(result1, result2)

    array = np.array([1, 2, 3])
    result1, result2 = squares(array), doubles(array)
    print(result1, result2)

    # [[], [], [], ...] (리스트 안의 리스트 구조)와 아래 df의 구조는 같다.
    # [1, 2], [3, 4], [5, 6]] == df
    # 그런데 DataFrame은 'squares()'함수를 적용 가능하지만,
    # 리스트안의 리스트 구조는 'squares()'함수를 적용 할 수 없다.
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6]
    })
    print(df)
    print(squares(df))

    result = df.apply(squares, axis=1)
    print(result)

    print(np.sum([1, 2, 3]))
    result = df.apply(np.sum, axis=1) # axis=0 : 컬럼을 함수에 전달 / axis=1 : row를 함수에 전달
    print(result)

    emp = pd.read_csv('emp_df.csv')
    emp.apply()