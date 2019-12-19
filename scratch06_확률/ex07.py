"""
<중심 극한 정리>
= 모집단이 어떤 분포든지 상관없이 표본의 크기가 충분히 크다면 모든 가능한 표본 평균은 모평균 주위에서 정규 분포를 따른다.

전체 인구 : 모집단(전체 집합) / 모평균 : 모집단(전체 집합)의 평균
전체 인구 중 일부 : 표본(부분 집합) / 표본 평균 : 표본(부분 집합)의 평균
즉, 부분집합(표본 평균)의 평균은 전체 집합의 평균(모평균) 주위에서 정규 분포를 따른다.

만약 모집단 평균이 'mu'이고, 표준 편차가 'sigma'인 정규 분포를 따른다면,
표본 평균의 분포는 평균이 'mu'이고, 분산이 'sigma/sqrt(n)'인 정규 분포이다.

- 베르누이 확률 변수
    = 어떤 시행의 결과가 '성공' / '실패'중 하나로 나타나고,
    성공의 확률이 'p' / 실패의 확률이 '1-p'라 할 때,
    그 결과가 '성공'이면 '확률 변수'는 '1'을,
    결과가 '실패'라면 '확률 변수'는 '0'을 갖는 확률 변수 X

- 베르누이 확률 질량 함수(PMF, Probability Mass Function)
    pmf(x) = p if x = 1, 1 - p if x = 0
           = (p**x) * ((1-p)**(1-x))

    ~ 이항 확률 변수(binomial random variable)
        n개의 독립적인 베르누의 확률 변수들을 더한 것.
    (EX)
        베르누이 확률 변수 -> 동전 1개를 던질 때 앞면의 수
        이항 확률 변수 -> 동전 1개를 n번 던질 때 앞면의 수

    ~ 베르누이 확률 변수의 기대값(평균) = p, 표준 편차 = sqrt(p(1-p))

    ~ 중심 극한 정리
    : n이 적당히 크다면, 이항 확률 변수의 분포는 대략 평균이 '(n*p)'이고,
      표준 편차가 'sqrt(n*p(1-p))'인 정규 분포의 확률 변수와 같다.

<<<중심 극한 정리의 핵심>>>
~~~> 표본의 평균(np)와 분산(np(1-p))을 알면, 모집단의 평균(p)와 분산(p(1-P))를 예측 가능하다.
"""
import math
import random
from collections import Counter
import matplotlib.pyplot as plt

from scratch06_확률.ex06 import normal_cdf, normal_pdf


def bernoulli_trial(p):
    """
    베르누이 확률 변수 0 또는 1을 확률 p에 따라 리턴함
    :param p: 확률
    :return: 베르누이 확률 변수(0 또는 1)
    """
    x = random.random() # random() ~> 0 ~ 1 사이의 난수 리턴
    return 1 if x < p else 0 # 생성된 난수가 확률 p보다 작으면 1, 크다면 0 리턴

def binomial(n, p):
    """
    1이 나올 확률이 p인 베르누이 시행을 n번 실시 했을 때, 1아 나오는 횟수를 리턴(이항 확률 변수를 리턴)
    :param n: 횟수
    :param p: 확률
    :return: 1이 나온 횟수(이항 확률 변수)
    """
    s = 0 # 1이 나오는 횟수
    for _ in range(n):
        s += bernoulli_trial(p)
    return s


if __name__ == '__main__':
    for _ in range(10):
        print(bernoulli_trial(0.5), end='') # 확률 p = 0.5
    print() # 0110000101

    for _ in range(10):
        print(binomial(10, 0.5), end='') # 10개의 동전을 던지고 앞면(1) 나올 확률 0.5
    print() # 5862678543 ~~~> 앞면(1)이 나오는 횟수가 10개 중 5번, 8번, 6번, 2번, ...

    trials = 10000
    data = [binomial(1, 0.5) for _ in range(10000)] # 동전 1개를 1번 던지기를 10000번. 앞면(1) 나올 확률은 0.5
    print(data[0:10]) # [0, 0, 1, 0, 1, 0, 1, 0, 1, 1]

    # 이항 확률 변수와 그에 따른 확률 값을 그리기 위해
    # pyplot.hist() 사용하여 히스토그램 출력
    #plt.hist(data)
    #plt.show()

    # pyplot.hist()없이 직접 그려보려면
    histogram = Counter(data)
    x_bar = [k for k in histogram.keys()]
    y_bar = [v / trials for v in histogram.values()]

    plt.bar(x_bar, y_bar)
    plt.show()

    trials = 10000
    data_3 = [binomial(3, 0.5) for _ in range(trials)]  # 동전 3개를 1번 던지기를 10000번. 앞면(1) 나올 확률은 0.5
    histogram = Counter(data_3)
    x_bar = [k for k in histogram.keys()]
    y_bar = [v / trials for v in histogram.values()]

    plt.bar(x_bar, y_bar)
    plt.show()

    trials = 10000
    data_12 = [binomial(12, 0.5) for _ in range(trials)]  # 동전 12개를 1번 던지기를 10000번. 앞면(1) 나올 확률은 0.5
    histogram = Counter(data_12)
    x_bar = [k for k in histogram.keys()]
    y_bar = [v / trials for v in histogram.values()]

    plt.bar(x_bar, y_bar)
    plt.show()
    # ~~~~~> 동전 개수가 늘어날수록, 그래프가 '정규 분포형'에 가까워진다.

    trials = 10000
    n = 4 #동전 던지는 횟수
    p = 0.5 # 동전 앞면(1)이 나오는 횟수
    data = [binomial(n, p) for _ in range(trials)]
    histogram = Counter(data)
    x_bar = [k for k in histogram.keys()]
    y_bar = [v / trials for v in histogram.values()]
    plt.bar(x_bar, y_bar)

    # 이항 확률 변수의 정규 분포 근사
    # 이항 확률 변수는 n이 충분히 크다면 정규 분포를 따른다.
    mu = n * p # 평균
    sigma = math.sqrt(n * p * (1 - p)) # 표준 편차
    # 정규 분포 그래프 그리기위해
    x_line = range(min(data), max(data) + 1)
    y_line = [normal_cdf(x + 0.5, mu, sigma) - normal_cdf(x - 0.5, mu, sigma) for x in x_line] # 확률 변수에 따른 누적 확률 값

    plt.plot(x_line, y_line)
    plt.show()

    # 그렇다면 동전을 100개로 늘려보자.
    trials = 10000
    n = 100  # 동전 던지는 횟수
    p = 0.5  # 동전 앞면(1)이 나오는 횟수
    data = [binomial(n, p) for _ in range(trials)]
    histogram = Counter(data)
    x_bar = [k for k in histogram.keys()]
    y_bar = [v / trials for v in histogram.values()]
    plt.bar(x_bar, y_bar)

    mu = n * p  # 평균
    sigma = math.sqrt(n * p * (1 - p))  # 표준 편차
    x_line = range(min(data), max(data) + 1)
    y_line = [normal_cdf(x + 0.5, mu, sigma) - normal_cdf(x - 0.5, mu, sigma) for x in x_line]  # 확률 변수에 따른 누적 확률 값

    plt.plot(x_line, y_line)
    plt.show()
    # ~~~~~> n이 크게 증가하자, 그래프가 정규 분포형에 매우 가까워졌다.

    # PDF를 사용하면, cdf보다 더 간단하다.
    trials = 10000
    n = 100  # 동전 던지는 횟수
    p = 0.5  # 동전 앞면(1)이 나오는 횟수
    data = [binomial(n, p) for _ in range(trials)]
    histogram = Counter(data)
    x_bar = [k for k in histogram.keys()]
    y_bar = [v / trials for v in histogram.values()]
    plt.bar(x_bar, y_bar)

    mu = n * p  # 평균
    sigma = math.sqrt(n * p * (1 - p))  # 표준 편차
    x_line = range(min(data), max(data) + 1)
    y_line = [normal_pdf(x, mu, sigma) for x in x_line] 

    plt.plot(x_line, y_line)
    plt.show()






