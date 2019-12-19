"""
단순 선형 회귀 : f(x) = b + a1 * x1
다중 선형 회귀 : f(x) = b + (a1 * x1) + (a2 * x2)
비 선형 회귀 : f(x) = b + (a1 * x) + (a2 * x^2)

비 선형 회귀에서 b / a1 / a2는 선형회귀를 사용해 결정 할 수 있다.

y = b + a1 * x1 + a2 * x2 ~> 선형 회귀
y = b + (a1 * x1) + (a2 * x2)+ (a3 * x1^2) + (a4 * x1 * x2) + (a5 * x2^2) ~> 비선형 회귀

선형 회귀에서의 방법과 마찬가지로, ('x1' / 'x2'에 대해 각각 기울기(계수)를 구했던 것처럼)
'x1' / 'x2' / 'x1^2' / 'x1*x2' / 'x2^2'의 경우에 대해 각각의 기울기(계수)를 구해주면 된다.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures # 변수들을 다항식으로 전처리하는 모듈

# 1. X(data)와 y(target) 생성
np.random.seed(1216)
X = 6 * np.random.rand(100, 1) - 3 # -3 <= X1 < 3 범위의 100개 숫자
print(X[:5])

y = 0.5 + 2 * X + X**2 + np.random.randn(100, 1)
# np.random.randn(100, 1) : 테스트를 위해 결과를 일부러 조금 다르게 하기위한 항
print(y[:5])

# 2. data와 target 그래프
plt.scatter(X, y)
plt.show()
# ~> 2차 함수의 형태 확인 가능. 따라서 예측시, 선형 회귀의 직선 형태는 맞지 않음.

# 3. 변수들을 다항식으로 전처리. PolynomialFeatures() ~~~> 입력값을 다차항식으로 변환
# ex) [x1,x2] ---> [1, x1, x2, x1^2, x2^2, x1x2]
poly_feature = PolynomialFeatures(degree=2, include_bias=False) # PolynomialFeatures() 객체 생성.
# ~~~> degree : n차항(default 2) / include_bias : 상수항 생성 여부(default True)

A = np.array([[1], [2], [3]])
A_poly = poly_feature.fit_transform(A)
print('A_poly : ', A_poly)
# A_poly :  [[1. 1.]
#  [2. 4.]
#  [3. 9.]]

B = np.array([[1, 2], [3, 4]])
B_poly = poly_feature.fit_transform(B)
print('B_poly : ', B_poly)
# B_poly :  [[ 1.  2.  1.  2.  4.]
#  [ 3.  4.  9. 12. 16.]]
# ~> [x1, x2, x1^2, x1x2, x2^2]의 형태

X_poly = poly_feature.fit_transform(X)
print('X_poly : ', X_poly[:5])
# X_poly :  [[ 2.9735891   8.84223212]
#  [ 0.74046546  0.5482891 ]
#  [ 2.25656212  5.09207262]
#  [ 2.33626717  5.45814428]
#  [-0.67942513  0.46161851]]

# 4. 모델 훈련.
lin_reg = LinearRegression() # 변환된 다차항 X를 LinearRegression()에 적용하기 위한 객체 생성
lin_reg.fit(X_poly, y)

# 4-1) y절편과 기울기 확인
print('y 절편 intercept : ', lin_reg.intercept_) # y 절편 intercept :  [0.53611387]
print('기울기(계수) coefficients : ', lin_reg.coef_) # 기울기(계수) coefficients :  [[2.02456163 0.97973891]]

# 5. 예측을 위한 test_set 생성
X_test = np.linspace(-3, 3, 100).reshape(100, 1) # (-3 ~ 3)의 범위에서 동일한 간격의 100개 숫자 생성해 2차원 리스트로
print(X_test[:5])

# 5-1) test_set을 다항식으로 전처리
X_test_poly = poly_feature.fit_transform(X_test)

# 6. 예측 (다항식으로 전처리 된 X_test_poly를 사용해서)
y_pred = lin_reg.predict(X_test_poly)

# 7. 모델 평가 위한 그래프
plt.scatter(X, y) # 원본 data와 target
plt.plot(X_test, y_pred, 'r') # 정답 data와 예측한 target
plt.show()

