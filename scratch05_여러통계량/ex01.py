"""
통계

1) 중심 경향성 : 평균, 중앙값, 분위수(4분위, 100분위(퍼센트)), 최빈값(가장 자주 나오는 값)

2) 산포도 : 데이터가 평균(또는 중앙값)을 중심으로 얼마나 퍼져있는가?
~~~> 분산(var) / 표준편차(std) / 범위(range)

3)상관 관계 : 공분산(Cov, Covariance) / 상관 계수 (Corr, Correlation)
~~~> 공분산은 2개의 확률 변수간의 상관정도를 나타냄. 그런데 공분산에는 각 변수의 단위가 존재한다.
따라서 이 단위를 없애기 위해, (공분산 / 표준편차)를 해서 '상관 계수'를 구한다.
Corr(x, y) = Cov(x, y) / (std(x) * std(y)), -1 <= Corr <= 1

단, '상관 관계'는 '인과 관계'를 의미하지는 않는다.

<<<심슨의 역설>>>
= 각 부분에 대한 평균이 크다고 해서, 전체에 대한 평균까지 항상 큰 것은 아니다.
"""
# 평균 ------------------------------------------------------------------------
def mean(x):
    """
    n개의 원소를 가진 리스트 x의 평균을 계산해 리턴

    :param x: n개의 원소를 갖는 1차원 리스트
    :return: 리스트 원소들의 평균
    """
    total = 0
    for i in range(len(x)):
        total = total + x[i]
    mean = total / len(x)
    return mean

# 중앙 값 ------------------------------------------------------------------------
def median(x):
    """
    리스트 x를 정렬해서, 중앙값을 찾아 리턴
    x의 원소 개수 n이 짝수이면, 중앙값을 찾아 리턴
    n이 홀수이면 중아의 두개 값의 평균값을 리턴
    :param x: 원소 n개의 리스트
    :return: 중앙값
    """
    sorted_x = sorted(x, reverse=True) # 리스트 x를 오름차순 정렬
    if len(sorted_x) % 2 == 0: # x 원소 개수 n이 짝수면
        median_x = sorted_x[int(len(x) / 2)]
    else: # x 원소 개수 n이 홀수면
        median_x = (sorted_x[int(len(sorted_x) / 2) - 1] + sorted_x[int(len(sorted_x) / 2)]) / 2
    return median_x

# 분위 값 ------------------------------------------------------------------------
def quantile(x, p):
    """
    리스트 x의 p분위에 속하는 값을 리턴
    :param x: 원소 n개의 리스트
    :param p: 0 ~ 1.0 사이 값
    :return: 해당 분위 수(퍼센트)의 값
    """
    n = len(x)
    quan_x = int(n * p) # 해당 퍼센트의 인덱스
    sorted_x = sorted(x)
    return sorted_x[quan_x]

# 최다 빈도 값 ------------------------------------------------------------------------
def mode(x):
    """
    리스트 x에서 가장 자주 나타나는 값인 최빈 값을 리턴
    여러개의 최빈 값이 존재할 경우, 리스트로 리턴
    from collections import Counter

    :param x: 원소 n개인 1차원 리스트
    :return: 최빈 값들의 리스트
    """
    from collections import Counter

    counts = Counter(x) # Counter 객체 생성 ~~~> dict 형태(key:value)로 반환
    print(counts) # Counter({7: 3, 8: 3, 6: 1, 2: 1, 3: 1, 1: 1, 5: 1, 4: 1, 10: 1, 9: 1})

    print(counts.keys(), counts.values())
    # dict_keys([6, 2, 3, 1, 5, 4, 10, 9, 7, 8]) dict_values([1, 1, 1, 1, 1, 1, 1, 1, 3, 3])
    # key = 실제 데이터 / value = 빈도 수

    print(counts.items())
    # dict_items([(6, 1), (2, 1), (3, 1), (1, 1), (5, 1), (4, 1), (10, 1), (9, 1), (7, 3), (8, 3)])
    # (key, value) 형태의 tuple들의 리스트

    # 최빈 값을 찾으려면, 가장 높은 value의 key값을 찾으면 된다.
    max_count = max(counts.values()) # 빈도 수(value)의 최대 값
    freq = [] # 최빈값이 저장될 리스트

    for val, cnt in counts.items(): # tuple들의 리스트에서 (val은 key, cnt는 value)
        if cnt == max_count: # 빈도 수가 최대 빈도 수와 같으면
            freq.append(val) # 리스트에 추가
    return freq

    # list comprehension을 사용하면
    # return [val for val, cnt in counts.items()
    #          if cnt == max_count]

# 리스트 원소 범위 크기 ------------------------------------------------------------------------
def data_range(x):
     """

     :param x: 원소 n개인 1차원 리스트
     :return: 리스트 최대값 - 리스트 최소값
     """
     sorted_x = sorted(x)
     return sorted_x[len(x) - 1] - sorted_x[0]

# 편차(데이터 - 평균) ------------------------------------------------------------------------
def de_mean(x):
    """
    편차(데이터 - 평균)들의 리스트를 리턴

    :param x: 원소 n개인 1차원 리스트
    :return: 편차들의 리스트
    """
    mu = mean(x) # 평균
    return [x_i - mu for x_i in x] # 편차들의 리스트 [(x1 - mean), (x2 - mean), ..., (xi - mean)]

# 분산 ------------------------------------------------------------------------
def variance(x):
    """
    var = (x1 - mean)**2 + (x2 - mean)**2 + ... + (xn - mean)**2 / (n - 1)

    :param x: 원소 n개인 1차원 리스트
    :return: x의 분산 값
    """
    n = len(x) # 리스트 x의 원소 개수

    # x_bar = mean(x) # 리스트 x의 평균
    # var_x = sum([(x_i - x_bar) ** 2 for x_i in x]) / (n-1)

    # 또는

    deviations = de_mean(x) # 편차들의 리스트를 가져온다
    var_x = sum([d ** 2 for d in deviations]) / (n-1)

    return var_x

# 내적(각 요소를 곱해 모두 더함)을 이용한 분산 ------------------------------------------------------------------------
def var_dot(x):
    # scratch04_벡터및행렬연산.ex01에서 만든 dot() 함수와 de_mean() 함수를 사용해 분산을 계산
    from scratch04_벡터및행렬연산.ex01 import dot

    deviations = de_mean(x)
    n = len(x)

    return dot(deviations, deviations) / (n-1)

# 표준 편차 ------------------------------------------------------------------------
def standard_deviation(x):
    """
    std = math.sqrt(variance)

    :param x: 원소 n개인 1차원 리스트
    :return: x의 표준 편차
    """
    import math
    std_x = math.sqrt(variance(x))
    return std_x

# 공분산 ------------------------------------------------------------------------
def Covariance(x, y):
    """
    Cov = sum((xi - mean(x)) * (yi - mean(y))) / (n-1)
    :param x: 리스트 x
    :param y: 리스트 y
    :return: x, y의 공분산
    """
    from scratch04_벡터및행렬연산.ex01 import dot

    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

    # 또는

    # x_mean = mean(x) # x의 평균
    # y_mean = mean(y) # y의 평균
    #
    # x_deviations = [x_i - x_mean for x_i in x]
    # y_deviations = [y_i - y_mean for y_i in y]
    # sum_of_deviations = 0

    # for xd, yd in zip(x_deviations, y_deviations):
    #     sum_of_deviations += xd * yd

    # return sum_of_deviations / (n-1)

# 상관 계수 ------------------------------------------------------------------------
def Correlation(x, y):
    """
    Corr = Cov(x, y) / (std(x) * std(y))

    :param x: 리스트 x
    :param y: 리스트 ㅛ
    :return: x, y의 상관 계수
    """
    return Covariance(x, y) / (standard_deviation(x) * standard_deviation(y))

    # 또는
    # std_x = standard_deviation(x)
    # std_y = standard_deviation(y)

    # if std_x != 0 and std_y != 0:
    #     corr = Correlation(x, y) / (std_x * std_y)
    # else:
    #     corr = 0

    # return corr

# 실행 ------------------------------------------------------------------------
if __name__ == '__main__':
    x = [6, 2, 3, 1, 5, 4, 10, 9, 7, 8, 8, 8 , 7, 7]
    print(mean(x))
    print(median(x))
    print(quantile(x, 0.5))

    print(mode(x)) # [7, 8]

    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(data_range(x1))
    print(variance(x1))
    print(standard_deviation(x1))
    print(mean(x1))

    x2 = [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10]
    y2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    print(Covariance(x2, y2))
    print(Correlation(x2, y2))

    x3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    y3 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
    print(Covariance(x3, y3))
    print(Correlation(x3, y3))

