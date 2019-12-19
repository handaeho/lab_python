"""
가설(Hypothesis) & 통계적 추론(Inference)

- 귀무 가설(영가설, Null Hypothesis, H0)
- 대립 가설(Alternative Hypothesis, H1)
~> Ex)
    H0 = 동전을 던졌을 때, 앞면이 나올 확률 p는 1/2이다. (p == 1/2)
    H1 = 동전을 던졌을 대, 앞면이 나올 확률 p는 1/2이 아니다. (p != 1/2)
두 가설 중, 하나가 '거짓'임을 증명하면 나머지 하나는 '참'일 것.

일반적으로 주장하고 싶은 내용을 '대립 가설(H1)' / 기각하고자 하는 내용을 '귀무 가설(H0)'로 놓는다.
그리고 H0를 '참'으로 가정하고, H1의 '참/거짓' 여부를 판별한다.

또는

'귀무 가설'이 다음과 같다면,
H0 = 동전을 던졌을 때, 앞면이 나올 확률 p > 1/2
이것의 '대립 가설'은 다음과 같다.
H1 = 동전을 던졌을 때, 앞면이 나올 확률 p <= 1/2

어떤 하나의 가설을 세운 후, 그 가설이 '참'이거나 다른 하나가 '거짓'임을 밝히면 된다.
'참'이라는 뜻은 내가 추론한 '결과와 일치하는 것'이다. '거짓'은 추론 '결과와 일치하지 않는 것'이다.

실제의 가설이 '참'일 때, '가설을 기각하지 않으면' '정상'.
실제의 가설이 '거짓'일 때, '가설을 기각'하면 '정상'.

Type 1 error(제 1종 오류) = 실제 결과의 가설이 '참'일 때, 가설을 '기각'함.
Type 2 error(제 2종 오류) = 실제 결과의 가설이 '거짓'일 때, 가설을 '기각하지 않음'.

- 유의수준(Significance Level) = 제 1종 오류(type 1)가 발생 할 확률의 최대 허용 한계
    유의 수준(a, alpha) = 0.05(5%), 0.01(1%), ...
    유의 수준에 따라 가설의 기각 여부를 결정한다.

- 검정력(Power) = 1 - beta. H0(귀무 가설)의 잘못을 찾아낼 확률(H0가 거짓일 확률)
    beta ~> 가설이 거짓인데, 기각하지 못하는 확률
    검정력은 제 2종 오류(type 2)에서 사용.

<정리>
1) H0 : 동전의 앞면이 나올 확률 p == 1/2
2) H1 : 동전의 앞면이 나올 확률 p != 1/2
3) 유의 수준(alpha) : H0(영가설)가 '참'이지만, 가설을 '기각'할 가능성
4) beta : H0(영가설)가 '거짓'이지만, 가설을 '기각하지 않을' 가능성
5) 검증력(power of test) = 1 - beta

"""
import math

from scratch06_확률.ex06 import normal_cdf, inverse_normal_cdf


def normal_approximation_to_binomial(n, p):
    """
    이항 분포(n, p)를 정규 분포로 근사했을 때의 평균 / 표준편차
    """
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    return mu, sigma

# 확률 변수가 어떤 구간 안이나 밖에 존재할 확률
# P(X <= b), P(X >= a), P(a <= X <= b)
# scratch06에서 작성한 normal_cdf() 함수 이용

# P(X <= high) : 확률 변수 값이 특정 값보다 작거나 같을 확률 = cdf(high)
normal_probability_below = normal_cdf

# P(X > low) : 확률 변수 값이 특정 값보다 클 확률 = cdf(low)
def normal_probability_above(low, mu=0.0, sigma=1.0):
    return 1 - normal_cdf(low, mu, sigma)

# P(low < X < high) : 확률 변수 값이 특정 범위 안에 있을 확률 = P(X < high) - P(X < low)
def normal_probability_between(low, high, mu=0.0, sigma=1.0):
    return normal_cdf(high, mu, sigma) - normal_cdf(low, mu, sigma)

# P(X < low or X > high) : 확률 변수 값이 특정 범위 밖에 있을 확률(단, low < high)
def normal_probability_outside(low, high, mu=0.0, sigma=1.0):
    return 1 - normal_probability_between(low, high, mu, sigma)

# 확률이 주어 졌을때, 상한(upper bound) 또는 하한(lower bound)
# 또는 범위 (lower ~ upper bound)를 찾는 함수들

# P(X < ub) = prob이 주어졌을 때, 상한 ub를 찾는 함수
def normal_upper_bound(prob, mu=0.0, sigma=1.0):
    return inverse_normal_cdf(prob, mu, sigma)

# P(X > lb) = prob이 주어졌을 때, 하한 lb를 찾는 함수
# P(X < lb) = 1- prob이 주어졌을 때, 상한 lb를 찾는 함수
def normal_lower_bound(prob, mu=0.0, sigma=1.0):
    return inverse_normal_cdf(1 - prob, mu, sigma)

# P(lb < X < ub) = prob이라는 확률이 주어졌을 때,
# 평균을 중심으로 대칭이 되는 구간의 상한과 하한을 찾는 함수
def normal_two_sided_bounds(prob, mu=0.0, sigma=1.0):
    # 범위의 양쪽 끝(tail)에 해당하는 확률
    tail_prob = (1 - prob) / 2
    # 찾고자 하는 상한은 확률 a 이상을 갖는 하한을 찾으면 된다.

    # 즉, P(X > a) = tail_prob을 만족하는 하한 a를 찾는다.
    upper_bound = normal_lower_bound(tail_prob, mu, sigma)
    # 또는 P(X < b) = prob + tail_prob을 만족하는 상한 b를 찾으면 된다.
    # upper_bound = normal_upper_bound(prob + tail_prob, mu, sigma)

    # 찾고자 하는 하한은 확률 b 이하를 갖는 상한을 찾으면 된다.
    # 즉, P(X < b) = tail_prob을 만족하는 상한 b를 찾는다.
    lower_bound = normal_upper_bound(tail_prob, mu, sigma)

    return lower_bound, upper_bound

def two_sided_p_value(x, mu=0.0, sigma=1.0):
    """
    양측 검정에서 사용하는 p-value
    """
    if x >= mu:
        return normal_probability_above(x, mu, sigma) * 2
    else:
        return normal_probability_below(x, mu, sigma) * 2

def estimate_parameters(N, n):
    """
    표본(샘플)의 평균으로 모집단의 평균, 표준편차 추정하는 함수
    N = 실험 횟수
    n = 실험에서 발견된 횟수
   """
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_a, n_a, N_b,n_b):
    """
    :return: 표준 정규 분포에서 p-value를 계산할 수 있는 z 값
    """
    p_a, sigma_a = estimate_parameters(N_a, n_a)
    p_b, sigma_b = estimate_parameters(N_b, n_b)

    return (p_b - p_a) / math.sqrt(sigma_a**2 + sigma_b**2)

if __name__ == '__main__':
    # 동전을 던졌을 때, 앞면이 나올 확률은 1/2임을 실험하고자 한자.
    # 동전을 1,000번 던지는 실험 시, ~~~> 이항 분포
    # 앞면이 나오는 기대값 ~~~> 정규 분포(mu = np, sigma = sqrt(n * p * (1 - p)))

    # 귀무 가설(H0, 영가설)
    # H0 : p = 1/2
    # H0가 참이라는 가정에서, 동전 앞면이 나오는 확률의 평균과 표준편차는
    mu, sigma = normal_approximation_to_binomial(1000, 0.5)
    print(f'p = 0.5라고 가정 = , mu_0 = {mu}, sigma_0 = {sigma}')
    # ~~~> p = 0.5라고 가정 = , mu_0 = 500.0, sigma_0 = 15.811388300841896

    # 유의 수준 5% : H0가 '참'이지만 '기각'하는 오류의 허용 범위가 5%. (type 1의 허용 범위 = 5%)
    # H0를 기각하지 않을 95% 확률의 상한 / 하한을 찾음
    low, high = normal_two_sided_bounds(0.95, mu, sigma)
    print(f'low = {low} / high = {high}')
    # ~~~> 유의 수준 5% 하에서, 1000번 던져 앞면이 나올 최소 횟수는 low / 최대 횟수는 high이다.
    # low = 469.01026640487555 / high = 530.9897335951244

    # 양측 검정
    # 만약, 동전 앞면이 나올 확률이 0.5가 아닌, 0.55라고 더 큰 확률로 '틀리게' 가정했을 때, 평균 / 표준편차
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
    print(f'p = 0.55라고 가정 = , mu_1 = {mu_1}, sigma_1 = {sigma_1}')
    # ~~~> p = 0.55라고 가정 = , mu_1 = 550.0, sigma_1 = 15.732132722552272

    # 그렇다면, p = 0.5라는 가정에서의 95% 구간이 p = 0.55라는 가정에서 나올 확률?
    beta = normal_probability_between(low, high, mu_1,sigma_1)
    print('beta = ', beta) # beta =  0.11345199870463285
    power = 1 - beta
    print('power = ', power) # power =  0.8865480012953671
    # 즉, beta는 약 0.113 ~~~> 틀린 가정을 맞다고 잘못 인식할 오류 발생 확률이 약 0.113
    #     power은 약 0.886 ~~~> 틀린 가정을 틀리다고 검증 할 수 있는 확률이 약 0.886

    # 그렇다면 이번에는 p = 0.5가 아닌 p = 0.45라고 더 작은 확률로 '틀리게' 가정해보면,
    mu_2, sigma_2 = normal_approximation_to_binomial(1000, 0.45)
    print(f'p = 0.45라고 가정 = , mu_1 = {mu_2}, sigma_1 = {sigma_2}')
    # ~~~> p = 0.45라고 가정 = , mu_1 = 450.0, sigma_1 = 15.732132722552274

    # p = 0.45라고 가정했을 때, beta / power?
    beta_2 = normal_probability_between(low, high, mu_2, sigma_2)
    print('beta = ', beta_2) # beta =  0.11345199870463285
    power_2 = 1 - beta_2
    print('power = ', power_2) # power =  0.8865480012953671
    # p = 0.55의 가정과 p = 0.45의 beta / power은 같다. (검정 능력이 같다.)
    # ~~~> 아래 넓이가 같은 그래프를 같은 차이로 평행 이동 했기 때문에, p = 0.5의 가정 그래프와 겹치는 구간 또한 같다.

    # 단측 검정 ~~~> 한 쪽으로만 치우치게 모델을 세워, 가설을 검증하는 것.
    # H0 : P <= 0.5
    # H1 : p > 0.5
    # 유의수준(5%)을 양끝에 2.5%씩이 아닌, 한쪽으로 모두 치우치게 해서, 원래의 가설에 대한 그래프와 겹치는 넓이를 줄인다.
    # p = 0.5일 때, 유의수준(5%)의 upper_bound 구간을 찾자.
    high = normal_upper_bound(0.95, mu, sigma)
    print('유의 수준 5%의 상한 = ', high) # 유의 수준 5%의 상한 =  526.0073585242053

    beta_3 = normal_probability_below(high, mu_1, sigma_1) # p = 0.55 가설의 경우
    power_3 = 1 - beta_3
    print(f'p = 0.55 가설의 경우 beta = {beta_3} / power = {power_3}')
    # ~~~> p = 0.55 가설의 경우 beta = 0.06362051966928262 / power = 0.9363794803307174
    # 따라서 검정력(power)이 커졌으므로, 기각 할 수 있다.

    # 그렇다면, 반대로 생각해보자.
    # H0 : p >= 0.5
    # H1 : p < 0.5
    # p = 0.5일 때, 유의수준(5%)의 lower_bound 구간을 찾자.
    low = normal_lower_bound(0.95, mu, sigma)
    print('유의 수준 5%의 하한 = ', low) # 유의 수준 5%의 하한 =  473.99264147579476

    beta_4 = normal_probability_above(low, mu_2, sigma_2) # p = 0.45 가설의 경우
    power_4 = 1 - beta_4
    print(f'p = 0.45 가설의 경우 beta = {beta_4} / power = {power_4}')
    # ~~~> p = 0.45 가설의 경우 beta = 0.06362051966928228 / power = 0.9363794803307177
    # p = 0.55 가설의 결과와 같다.

    # p-value : H0(영가설)가 '참'이라고 가정 시, 실험 관측값보다 더 극단적인 값이 관측될 확률.
    # 'p-value(극단적인 값이 나올 확률)'가 '유의수준보다 작다'면, 그 값은 '우연히 발생한 값'이라고 '말할 수 있다'.
    # 'p-value(극단적인 값이 나올 확률)'가 '유의수준보다 크다'면, 그 값은 '우연히 발생한 값'이라고 '말할 수 없다'.
    # 즉, p-value > 유의 수준 ~~~> 우연히 발생 X => H0 기각 X
    # p-value < 유의 수준 ~~~> 우연히 발생 => H0 기각 O

    # 동전을 1000번 던지는 실험에서 동전의 앞면이 530번 나왔다.

    # '양측 검정'시의 H0 : p = 0.5 / H1 : p != 0.5
    p_value = two_sided_p_value(530, mu, sigma)
    print(p_value) # 0.05777957112359733 > 유의 수준(0.05)

    # 만약 우리가 동전을 던져 앞면이 나올 확률 p는 0.5에 근사함을 모르는 상태에서, (모집단을 모름)
    # 동전을 1000번 던져서 앞면이 525번이 나왔다.
    # 이 사실만으로 앞면의 확률 p = 525/1000 = 0.525로 설정하였다.
    p_bar = 525 / 1000
    mu = p_bar # 모집단의 평균을 실험 값(표본)의 평균으로 대체
    sigma = math.sqrt(p_bar * (1 - p_bar) / 1000) # 모집단의 표준 편차를 표본의 표준 편차로 추정
    bounds = normal_two_sided_bounds(0.95, mu, sigma) # 동전의 앞면이 나올 확률의 하한 / 상한
    print(bounds) # (0.4940490278129096, 0.5559509721870904)
    # 실험을 통해서 찾은 95% 신뢰 구간 (약 0.494 ~ 0.555)
    # -> 진짜 p값(0.5, 앞면이 나올 진짜 확률)은 위 구간에 포함 되며, 이는 95% 확신할 수 있다.

    # 이번에는 다른 실험에서 동전을 1000번 던졌을 때, 앞면이 540번이 나왔다.
    # p = 540/1000 = 0.54
    p_bar = 540 / 1000
    mu = p_bar
    sigma = math.sqrt(p_bar * (1 - p_bar) / 1000)
    bounds = normal_two_sided_bounds(0.95, mu, sigma)
    print(bounds) # (0.5091095927295919, 0.5708904072704082)
    # 실험을 통해서 찾은 95% 신뢰 구간 (약 0.509 ~ 0.570)
    # -> 진짜 p값(0.5, 앞면이 나올 진짜 확률)은 위 구간에 포함되지 않는다.

    # A / B TEST
    # 1000명 중, 200명이 본 A 광고와 1000명 중 180명이 본 B 광고는 홍보 효과의 차이가 있을까?
    # N_a = 1000, n_a = 200, N_b = 1000, n_b = 180
    z1 = a_b_test_statistic(1000, 200, 1000, 180)
    print('z1 = ', z1) # z1 = -1.1403464899034472
    p_value_1 = two_sided_p_value(z1)
    print('p_value = ', p_value_1) # p_value = 0.254141976542236. 또한 p_value > 0.05(유의수준 5%)
    # 우리는 A, B 광고 효과의 차이가 '있다고 가정'했다. 즉, H1은 '광고 효과 차이가 있음'.
    # 그런데 'p_value > 유의 수준'이므로, H0를 기각 하지 않는다. (H0는 '광고 효과 차이가 없음')
    # 다시 말해, 따라서 두 광고 간의 효과 차이가 거의 없다고 말할 수 있다.

    # 그럼 B 광고를 1000명 중 150명이 봤다면 차이가 나려나?
    z2 = a_b_test_statistic(1000, 200, 1000, 150)
    print('z2 = ', z2)  # z2 =  -2.948839123097944
    p_value_2 = two_sided_p_value(z2)
    print('p_value = ', p_value_2) # p_value =  0.003189699706216853. p_value < 0.05 (유의 수준 5%)
    # 'p_value < 유의 수준'이므로, H0를 기각한다. (H0는 '광고 효과 차이가 없음')
    # 다시 말해, 따라서 '두 광고 간의 효과 차이가 있다'는 우리의 H1 가설을 채택할 수 있다.

