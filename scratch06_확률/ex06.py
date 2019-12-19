"""
<<<연속 확률 분포>>>

1) 확률 밀도 함수(PDF, Probability Density Function)
~~~> 특정 확률 변수 구간을 적분 한 값(확률 밀도 함수 아래 면적)으로 확률을 계산 할 수 있는 함수
    P(a <= x < b) = Integral from a to b [pdf(x)dx]
2) 누적 분포 함수(CDF, Cumulative Distribution Function)
~~~> 확률 변수의 값이 특정 값보다 작거나 같을 확률을 나타내는 함수
    cdf(x) = P(x <= b)

P(a<= x < b) = P(x < b) - P(x <= a)
"""
import matplotlib.pyplot as plt
import math

def uniform_pdf(x):
    """
    Uniform Distribution(균등 분포) 확률 밀도 함수
    """
    return 1 if 0 <= x < 1 else 0

def uniform_cdf(x):
    """
    균등 분포 누적 분포 함수
    """
    if x < 0:
        return 0
    elif 0 <= x < 1:
        return x
    else:
        return 1

SQRT_TWO_PI = math.sqrt(2 * math.pi)
def normal_pdf(x, mu=0, sigma=1.0):
    """
    평균이 'mu'이고 표준편차가 'sigma'인 정규 분포 확률 밀도 함수
    """
    # math.exp() ~~~> 지수 함수 e
    return math.exp(-(x - mu)**2 / 2 * (sigma**2)) / (SQRT_TWO_PI * sigma) # 정규 분포 공식


def normal_cdf(x, mu=0.0, sigma=1.0):
    """
    평균이 'mu'이고 표준편차가 'sigma'인 정규 분포의 누적 분포 함수
    """
    # math.erf() 함수 ~~~> 누적 분포 함수
    return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2

def inverse_normal_cdf(p, mu=0.0, sigma=1.0, tolerance=0.00001):
    """
    누적 확률 p를 알 때, 정규 분포 확률 변수 x는?
    """
    # 표준 정규 분포가 아니라면 표준 정규 분포로 변환(표준 정규 분포 ~~~> mu = 0.0 / sigma = 1.0인 상태)
    if mu != 0.0 or sigma != 1.0:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance) # 재귀함수 사용
    low_z, low_p = -10.0, 0.0
    high_z, high_p = 10.0, 1.0
    while high_z - low_z > tolerance:
        mid_z = (low_z + high_z) / 2.0 # 중간 값
        mid_p = normal_cdf(mid_z) # 중간 값에서의 누적 확률
        if mid_p < p: # 중간 누적 확률이 전달 받은 확률보다 낮으면
            low_z = mid_z # 최소 값에 중간 값을
        else: # 중간 누적 확률이 전달 받은 확률보다 높으면
            high_z = mid_z # 최대 값에 중간값을
    # 반복하면서, 계속 low ~ high 구간을 줄여나가며 mid_z를 찾는 것.
    # 2진 탐색 정렬 알고리즘과 유사하다. (중간 값을 찾고, 업/다운. 다시 그 구간의 중간 값을 찾고 업/다운, ...)
    return mid_z


if __name__ == '__main__':
    # -2 <= x <= 2 구간을 0.1씩 나눔
    xs = [x/10 for x in range(-20, 21)]
    print(xs) # [-2.0, -1.9, -1.8, ..., 2.0]

    ys = [uniform_pdf(x) for x in xs]
    # xs의 값중에서 0 <= x < 1이면 y=1을, 아니라면 y=0을 리턴
    print(ys) # [...,0, 0, 0, ..., 1, 1, 1, 1, 1, 1, ..., 0, 0, 0]

    plt.plot(xs, ys)
    plt.title('Uniform Distribution')
    plt.show()

    ys = [uniform_cdf(x) for x in xs]
    # # xs의 값중에서 0 <= x < 1이면 x를(y=x), x<0이라면 0을(y=0), 아니라면(x>=1) 1을(y=1) 리턴
    plt.plot(xs, ys)
    plt.title('Uniform Distribution CDF')
    plt.show()

    # -5 <= x <= 5 구간을 0.1씩 나눔
    xs1 = [x / 10 for x in range(-50, 51)]
    print(xs1)  # [-5.0, -4.9, -4.8, ..., 4.9, 5.0]

    # mu = 0.0 / sigma = 1.0인 정규 분포 그래프
    # mu(평균)를 기준으로 좌우 대칭인 그래프. 또한 sigma가 커질수록 그래프 간격이 좁아짐
    ys2 = [normal_pdf(x) for x in xs1]
    ys3 = [normal_pdf(x, sigma=2.0) for x in xs1]
    ys4 = [normal_pdf(x, sigma=0.5) for x in xs1]

    ys5 = [normal_pdf(x, mu=-1) for x in xs1]

    plt.plot(xs1, ys2, '-', label='mu=0, sigma=1')  # 여러 그래프 한 번에 출력하기 위해 label 설정
    plt.plot(xs1, ys3, '--', label='mu=0, sigma=2')
    plt.plot(xs1, ys4, ':', label='mu=0, sigma=0.5')

    plt.plot(xs1, ys5, '-.', label='mu=-1, sigma=1.0')

    plt.legend() # 설정한 label 호출
    plt.title('Normal Distribution PDF')
    plt.show()

    # 정규 분포의 누적 분포 함수 그래프
    ys1 = [normal_cdf(x) for x in xs1]
    ys2 = [normal_cdf(x, sigma=2.0) for x in xs1]
    ys3 = [normal_cdf(x, sigma=0.5) for x in xs1]

    ys4 = [normal_cdf(x, mu=-1) for x in xs1]

    plt.plot(xs1, ys1, '-', label='mu=0, sigma=1.0')
    plt.plot(xs1, ys2, '--', label='mu=0, sigma=2.0')
    plt.plot(xs1, ys3, ':', label='mu=0, sigma=0.5')

    plt.plot(xs1, ys4, '-.', label='mu=-1, sigma=1.0')

    plt.legend()
    plt.title('Normal Distribution CDF')
    plt.show()

    # 누적 확률 p를 알 때, 정규 분포 확률 변수 x
    # P = 0.9, 0.99, 0.999인 확률 변수 x
    x1 = inverse_nomal_cdf(p=0.9)
    print('x1 = ', x1) # x1 =  1.2815570831298828
    x2 = inverse_nomal_cdf(p=0.99)
    print('x2 = ', x2) # x2 =  2.326345443725586
    x3 = inverse_nomal_cdf(p=0.999)
    print('x3 = ', x3) # x3 =  3.090238571166992
