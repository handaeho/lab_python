"""
선형 회귀(Linear Regression) : y = b + ax
"""
from sklearn import linear_model
from sklearn.datasets import load_diabetes

import matplotlib.pyplot as plt
import numpy as np


# 데이터 load
datasets = load_diabetes()
X = datasets.data
y = datasets.target

# 데이터를 load하고, 동시에 데이터와 레이블로 구분하게 되면,
# X, y = load_diabetes(return_X_y=True)
# print(X.shape, y.shape) # (442, 10) (442, )
# 단, 이 방식으로 load하게 되면, 컬럼 이름을 알 수 없다.

print(X.shape, y.shape) # (442, 10) (442,)

features = datasets.feature_names
print(features)
# ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

print(X[:1])
# [[0.03807591 0.05068012 0.06169621 0.02187235 -0.0442235 -0.03482076 -0.04340085 -0.00259226 0.01990842 -0.01764613]]
# 지금 데이터세트 자체가 평균 = 0, 표준편차 = 1로 전처리가 된 상태로 구성되어 있다.

print(y[:5]) # [151.  75. 141. 206. 135.]

# 각 특성별 그래프 그리기 ---> 1개의 figure에 10개의 subplot 출력(y ~ 10개 특성)
X_transpose = [column for column in zip(*X)]
# X_transpose = np.transpose(X)
# print('X_transpose shape:', X_transpose.shape)
print(X_transpose[0])

fig, ax = plt.subplots(3, 4)
for row in range(3):
    for col in range(4):
        axis = ax[row, col]
        idx = 4 * row + col
        if idx > 9:
            break
        x = X_transpose[idx]
        axis.scatter(x, y)
        axis.set_title(features[idx])
plt.show()

# ====================================================================

# BMI와 당뇨병의 선형 상관 관계 : f(x) ~ ax + b = a * bmi + b
# 데이터에서 bmi 데이터 추출.
bmi = X[:, np.newaxis, 2] # data에서 'bmi' 컬럼만 선택.
# np.newaxis -> 가상의 축을 생성해 1차원 배열을 2차원 배열로 만듦.
print(bmi[:5])
print('bmi shape : ', bmi.shape)
# [[ 0.06169621]
#  [-0.05147406]
#  [ 0.04445121]
#  [-0.01159501]
#  [-0.03638469]]
# bmi shape :  (442, 1)
# ~> 원소가 1개뿐인 리스트로 구성된 2차원 리스트 생성

# bmi(data)와 y(target)를 train_set / test_set으로 분리
bmi_train = bmi[:-40]
bmi_test = bmi[-40:]
y_train = y[:-40]
y_test = y[-40: ]

# 선형 회귀 모델 객체 생성
regr = linear_model.LinearRegression()

# 생성된 선형 회귀 모델 객체에 train_set을 적용한 학습(fit)
regr.fit(bmi_train, y_train)
# 1D array가 들어오면 'ValueError: Expected 2D array, got 1D array instead' 발생.
# ~> LinearRegression() 모엘에는 '2차원(2D) array'가 들어와야한다.
# 그래서 데이터에서 bmi를 추출할 때, 'np.newaxis'를 적용해 원소가 1개인 리스트로 이루어진 2차원 리스트로 구성한것.

# .fit() : f(x) ~ ax + b = a * bmi + b의 선형 관계식에서 y절편 'b'와 기울기 'a'를 결정
print('coefficients : ', regr.coef_)
# coefficients :  [955.44001079] ~~~> 기울기 'a'
print('intercept : ', regr.intercept_)
# intercept :  152.9043003554328 ~~~> y 절편 'b'

# 훈련된 모델을 사용한 예측 및 테스트
y_pred = regr.predict(bmi_test)
print(y_pred)

# 비교 그래프
# 실제 값
plt.scatter(bmi_test, y_test)
# 예측 값
plt.plot(bmi_test, y_pred, 'ro-')
plt.show()

# ====================================================================

# s5와 당뇨병의 선형 상관 관계 : f(x) ~ ax + b = a * s5 + b
# 데이터에서 s5 데이터 추출.
s5 = X[:, np.newaxis, -2] # data에서 'bmi' 컬럼만 선택.
# np.newaxis -> 가상의 축을 생성해 1차원 배열을 2차원 배열로 만듦.
print(s5[:5])
print('s5 shape : ', s5.shape)
# [[ 0.01990842]
# [-0.06832974]
# [ 0.00286377]
# [ 0.02269202]
# [-0.03199144]]
# s5 shape :  (442, 1)
# ~> 원소가 1개뿐인 리스트로 구성된 2차원 리스트 생성

# s5(data)와 y(target)를 train_set / test_set으로 분리
s5_train = s5[:-40]
s5_test = s5[-40:]
y_train = y[:-40]
y_test = y[-40: ]

# 선형 회귀 모델 객체 생성
regr = linear_model.LinearRegression()

# 생성된 선형 회귀 모델 객체에 train_set을 적용한 학습(fit)
regr.fit(s5_train, y_train)
# 1D array가 들어오면 'ValueError: Expected 2D array, got 1D array instead' 발생.
# ~> LinearRegression() 모엘에는 '2차원(2D) array'가 들어와야한다.
# 그래서 데이터에서 bmi를 추출할 때, 'np.newaxis'를 적용해 원소가 1개인 리스트로 이루어진 2차원 리스트로 구성한것.

# .fit() : f(x) ~ ax + b = a * s5 + b의 선형 관계식에서 y절편 'b'와 기울기 'a'를 결정
print('coefficients : ', regr.coef_)
# coefficients :  [899.53962949] ~~~> 기울기 'a'
print('intercept : ', regr.intercept_)
# intercept :  152.26618532091717 ~~~> y 절편 'b'

# 훈련된 모델을 사용한 예측 및 테스트
y_pred = regr.predict(s5_test)
print(y_pred)

# 비교 그래프
# 실제 값
plt.scatter(s5_test, y_test)
# 예측 값
plt.plot(s5_test, y_pred, 'ro-')
plt.show()

# ---------------------------------------------------------------------------
# Cf) .flatten() ~~~> 행렬의 차원 줄이기(평평하게 만들기)
array = np.array([[1, 2],
                  [3, 4]])
print(array) # 2x2 행렬
for row in range(2):
    for col in range(2):
        print(array[row, col], end=' ') # 1 2 3 4
print()

array_flatten = array.flatten() # array를 2차원을 1차원으로 평평하게(flatten)한다.
for i in range(4):
    print(array_flatten[i], end=' ') # 1 2 3 4

# flatten() 메소드를 이용해, 여러 그래프를 한 화면에 출력해보자
fig, ax = plt.subplots(3, 4) # 여기서 ax는 3x4 형태의 2차원 배열
ax_flatten = ax.flatten() # 2차원 배열 ax를 1차원 배열로 만듦.
for i in range(len(features)):
        subplot = ax_flatten[i]
        subplot.scatter(X[:, i], y)
        subplot.set_title(features[i])
plt.show()
# ---------------------------------------------------------------------------
