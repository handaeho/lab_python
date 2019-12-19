import numpy as np
import pandas as pd

def squared_mean(data):
    """ data를 제곱해, 평균을 계산 """
    squared_sum = 0
    for x in data:
        squared_sum += x ** 2

    return squared_sum / len(data)


def my_funx(x):
    return x.min(), x.max(), x.mean(), squared_mean(x)


if __name__ == '__main__':
    np.random.seed(1234)
    df = pd.DataFrame({
        'pop': np.random.randint(1, 10, 4),
        'income': np.random.randint(1, 10, 4)
    }, index=['a', 'b', 'c', 'd'])
    print(df)

    # agg(aggregate)(): DataFrame의 축(axis)을 기준으로 통계량을 집계(aggregate)하기 위한 함수
    # 통계량(statistics): 합계(sum), 평균(mean), 분산(var), 표준편차(std), 최솟값(min), 최댓값(max), 중앙값(median), ...
    # agg 함수는 집계가 목적이기 때문에 데이터 타입이 숫자 타입인 행/열에만 함수를 적용해서 계산함.
    # agg 함수는 pandas나 numpy에서 제공하는 집계 함수들 이외에도 사용자 정의 함수를 사용 가능.
    # 단, 함수는 Series를 파라미터에 전달하면 숫자(스칼라)를 리턴하는 함수여야만 한다.

    print(' === agg by column (axis=0) ===')
    print(df.agg('mean', axis=0)) # axis 파리미터의 default는 0
    # axis=0이면 column을 기준으로 함수에 전달해 계산한다.

    print(' === agg by row (axis=1) ===')
    print(df.agg('mean', axis=1))
    # axis=1이면 row를 기준으로 함수에 전달해 계산한다.

    print(df.agg(squared_mean, axis=0))
    # pop       31.5
    # income    49.5
    # ~~~> col을 함수에 전달
    print(df.agg(squared_mean, axis=1))
    # a    48.5
    # b    26.5
    # c    50.0
    # d    37.0
    # ~~~> row를 함수에 전달

    # apply() : DataFrame에 axis(축)을 기준으로 함수를 적용하기 위한 함수.
    # 적용하는 함수는 pandas 객체(DataFrame, Series, 스칼라)를 리턴하면 된다.
    # agg 함수는 숫자 타입 스칼라만 리턴하는 함수를 적용하는 apply의 특수한 경우,
    # apply() 함수는 agg() 함수보다 더 유연하게 사용 가능.
    # 그러나 집계 함수등에 한해서는 agg() 함수가 더 좋은 성능.

    print(' === apply by column (axis=0) ===')
    print(df.apply('mean'))
    #  === apply by column (axis=0) ===
    # pop       5.5
    # income    6.5

    print(' === apply by row (axis=1) ===')
    print(df.apply('mean', axis=1))
    #  === apply by row (axis=1) ===
    # a    6.5
    # b    4.5
    # c    7.0
    # d    6.0

    print(df.apply(my_funx))
    # pop       (4, 7, 5.5, 31.5)
    # income    (2, 9, 6.5, 49.5)
    print(df.apply(my_funx, axis=1))
    # a    (4, 9, 6.5, 48.5)
    # b    (2, 7, 4.5, 26.5)
    # c    (6, 8, 7.0, 50.0)
    # d    (5, 7, 6.0, 37.0)

    











