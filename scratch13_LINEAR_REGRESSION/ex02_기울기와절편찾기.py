import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# X, y 생성
np.random.seed(1216)
X = 2 * np.random.rand(100, 1)
print(X.shape) # (100, 1) ~> 2x1 행렬(2차원 ndarray), 데이터 0.0 ~ 2.0
y = 4 + 3 * X + np.random.randn(100, 1)
print(y.shape) # (100, 1)

# X, y 상관 관계 그래프
plt.scatter(X, y)
plt.show()

# X, y의 관계에서 f(X) ~ a * X + b를 만족하는 기울기 'a', y 절편 'b'를 찾아보자.
# y1 = a * X1 + b, y2 = a * X2 + b, ..., y100 = a * X100 + b

X_b = np.c_[np.ones((100, 1)), X]
# np.ones(100, 1) : 원소가 모두 1인 100x1 행렬 생성
# c_ : 컬럼을 기준으로 합친다.
print(X_b.shape) # (100, 2)
print(X_b[:5])
# [[1.         1.99119637]
#  [1.         1.24682182]
#  [1.         1.75218737]
#  [1.         1.77875572]
#  [1.         0.77352496]]

# linalg 모듈 : Linear Algebra(선형 대수)
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print('theta_best : ', theta_best)
# [[3.90187826] ~~~> y 절편
#  [3.07247138]] ~~~> 기울기
# ~~~> y = X * theta. theta = (X^T * X)^-1 * (X^T * y)
# X_B.T ---> X_b의 전치 행렬(행과 열을 바꿈)

# 행렬식을 이용해서 찾은 theta 값과 LinearRegression 클래스에서 계산된 theta 비교
lin_reg = LinearRegression() # LinearRegression() 객체 생성
lin_reg.fit(X, y) # 모델 학습
print(f'y 절편 = {lin_reg.intercept_} / 기울기 = {lin_reg.coef_}')
# y 절편 = [3.90187826] / 기울기 = [[3.07247138]]

# 행렬식: y = X_b @ theta
X_test = [[0], [1], [2]]
X_test_b = np.c_[np.ones((3, 1)), X_test]
print(X_test_b)
# [[1. 0.]
#  [1. 1.]
#  [1. 2.]] ~~~> X_test에 [[1], [1], [1]] 행렬이 컬럼 기준(세로로)으로 합쳐짐.

# 우리가 찾은 기울기 'a'와 y절편 'b'인 'theta_best'를 사용한 예측
y_pred = X_test_b.dot(theta_best)
print(y_pred)
# [[ 3.90187826]
#  [ 6.97434963]
#  [10.04682101]]

# 이번에는 scikit_learn 패키지의 linear_regression 모듈을 사용한 예측
predictions = lin_reg.predict(X_test)
print(predictions)
# [[ 3.90187826]
#  [ 6.97434963]
#  [10.04682101]]

# 두 값을 그래프로 비교
plt.scatter(X, y)
plt.plot(X_test, y_pred, 'r')
plt.plot(X_test, predictions, 'b')
plt.show()

