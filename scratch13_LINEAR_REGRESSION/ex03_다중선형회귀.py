"""
단순 선형 회귀 : f(x) = b + a1 * x1
다중 선형 회귀 : f(x) = b + (a1 * x1) + (a2 * x2) + ...
"""
import numpy as np
from sklearn.linear_model import LinearRegression


# 1) X(data), y(target) 생성
np.random.seed(1216)
X1 = np.random.rand(100, 1)
X2 = np.random.rand(100, 1)
print('X1 : ', X1[:5])
print('X2 : ', X2[:5])

y = 3 + 4 * X1 + 5 * X2 + np.random.rand(100, 1)
print('y : ', y[:5])

# 2) X1과 X2를 합침
X = np.c_[X1, X2]
print('X : ', X[:5])

# 3) LinearRegression() 모듈의 객체 생성
lin_reg = LinearRegression()

# 4) 모델 훈련(data와 target(정답))를 줌
lin_reg.fit(X, y)

# 5) y절편과 기울기 확인
print('y 절편 intercept : ', lin_reg.intercept_)
# y 절편 intercept :  [3.50034483]
print('기울기(계수) coefficients : ', lin_reg.coef_)
# 기울기(계수) coefficients :  [[4.03293037 4.98799123]] ~~~> 각각 X1, X2에 대한 기울기(계수)

# 이렇게 각각의 데이터(x 값)에 대한 기울기(계수)를 찾을수 있다. (y 절편은 공통)
