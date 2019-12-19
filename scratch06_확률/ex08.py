"""
scipy 패키지의 stats 모듈에서 제공하는
확률 밀도 함수(PDF, Probability Density Function)
누적 분포 함수(CDF, Cumulative Distribution Function)
"""
import scipy.stats as stats
import matplotlib.pyplot as plt

xs = [x / 10 for x in range(-30, 31)] # 그래프를 그릴 x 구간(-30 ~ 30, 0.1 단위)

# 균등 분포(uniform distribution) -----------------------------------------------------

# 균등 분포의 확률 밀도 함수(PDF)
ys1 = [stats.uniform.pdf(x) for x in xs] # xs의 구간 동안 '균등 분포 확률 밀도 함수(PDF)'에 따른 y 좌표

# 균등 분포 누적 분포 함수(CDF)
ys2 = [stats.uniform.cdf(x) for x in xs] # xs의 구간 동안 '균등 분포 누적 분포(CDF)' 함수에 따른 y 좌표

plt.plot(xs, ys1, color='b', label='PDF')
plt.plot(xs, ys2, color='r', label='CDF')
plt.legend()
plt.title('Uniform Distribution PDF & CDF')
plt.show()

# 정규 분포(normal distribution) -----------------------------------------------------

# 표준 정규 분포의 확률 밀도 함수(PDF) ~> default : mu = 0, sigma = 1.0
ys1 = [stats.norm.pdf(x) for x in xs] # xs의 구간 동안 '정규 분포 확률 밀도 함수(PDF)'에 따른 y 좌표

# 표준 정규 분포 누적 분포 함수(CDF)
ys2 = [stats.norm.cdf(x) for x in xs] # xs의 구간 동안 '정규 분포 누적 분포(CDF)' 함수에 따른 y 좌표
plt.plot(xs, ys1, color='b', label='PDF')
plt.plot(xs, ys2, color='r', label='CDF')
plt.legend()
plt.title('Standard Normal Distribution PDF & CDF')
plt.show()