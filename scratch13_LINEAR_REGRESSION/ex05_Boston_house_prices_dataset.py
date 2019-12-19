"""
scikit-learn 패키지의 Boston house prices dataset
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures


print('\n ------------------------------------------------------------------------------------------- \n')

# 1. Dataset load & X(data), y(target) 생성

boston_house_price = load_boston()
X = boston_house_price.data
y = boston_house_price.target

print(X.shape) # (506, 13)
print(y.shape) # (506, )
print(boston_house_price['DESCR']) # 데이터 세트에 대한 명세(설명)

features = boston_house_price.feature_names
print(features)
# ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']

print('\n ------------------------------------------------------------------------------------------- \n')

# 2. data와 target 그래프

X_transpose = [column for column in zip(*X)]

fig, ax = plt.subplots(4, 4)
ax_flat = ax.flatten()
for i in range(len(features)):
    axis = ax_flat[i]
    axis.scatter(X[:, i], y)
    axis.set_title(features[i])
plt.show()

print('\n ------------------------------------------------------------------------------------------- \n')

# 3. train_set / test_set 구성

np.random.seed(1217)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print(f'X_train len : {len(X_train)} / X_test len : {len(X_test)}')
# X_train len : 354 / X_test len : 152

print('\n ------------------------------------------------------------------------------------------- \n')

# 4. train_set을 사용해 선형 회귀 모델 학습 - 단순 선형 회귀 / 다중 선형 회귀

lin_reg = LinearRegression() # ~~~~~> 선형 회귀 객체 생성

# 4-1) 단순 선형 회귀
# price(y) ~ b0(y 절편) + b1(기울기) * RM(방 개수) ----------------------------------------------------
X_train_rm = X_train[:, np.newaxis, 5] # 'RM' 컬럼 사용하고, 2차원 배열 형태로 만듦.
X_test_rm = X_test[:, np.newaxis, 5]
print(f'X_train_rm : {X_train_rm.shape} / X_test_rm : {X_test_rm.shape}')
# X_train_rm : (354, 1) / X_test_rm : (152, 1)

lin_reg.fit(X_train_rm, y_train) # 모델 학습 -> y 절편(b0), 기울기(b1)를 찾는다
print('단순 선형 회귀 RM coefficients : ', lin_reg.coef_) # 단순 선형 회귀 RM coefficients :  [9.67174089]
print('단순 선형 회귀 RM intercept : ', lin_reg.intercept_) # 단순 선형 회귀 RM intercept :  -38.625495771022045

y_pred_rm = lin_reg.predict(X_test_rm)
print(y_pred_rm[:5])

plt.scatter(X_test_rm, y_test) # ~~~> 실제 값
plt.plot(X_test_rm, y_pred_rm, 'r') # ~~~> 예측 값
plt.show()

# price(y) ~ b0(y 절편) + b1(기울기) * LSTAT(최저인구수) ----------------------------------------------------
X_train_lstat = X_train[:, np.newaxis, 12] # 'LSTAT' 컬럼 사용하고, 2차원 배열 형태로 만듦.
X_test_lstat = X_test[:, np.newaxis, 12]
print(f'X_train_rm : {X_train_lstat.shape} / X_test_rm : {X_test_lstat.shape}')
# X_train_rm : (354, 1) / X_test_rm : (152, 1)

lin_reg.fit(X_train_lstat, y_train) # 모델 학습 -> y 절편(b0), 기울기(b1)를 찾는다
print('단순 선형 회귀 LSTAT coefficients : ', lin_reg.coef_) # 단순 선형 회귀 LSTAT coefficients :  [-0.95632576]
print('단순 선형 회귀 LSTAT intercept : ', lin_reg.intercept_) # 단순 선형 회귀 LSTAT intercept :  34.499369101945064

y_pred_lstat = lin_reg.predict(X_test_lstat)
print(y_pred_lstat[:5])

plt.scatter(X_test_lstat, y_test) # ~~~> 실제 값, 실제 값
plt.plot(X_test_lstat, y_pred_lstat, 'r') # ~~~> 실제 값, 예측 값
plt.show()

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n')

# 4-2) 다중 선형 회귀
# 다차항 price ~ LSTAT + LSTAT^2 ----------------------------------------------------
# price(y) ~ b0(y 절편) + b1(기울기) * (LSTAT(최저인구수) + b2) * LSTAT^2
poly = PolynomialFeatures(degree=2, include_bias=False) # 다항식으로 만들기 위한 모듈인 PolynomialFeatures 객체 생성
# ~> 데이터에 다항식 항을 컬럼으로 추가한다. 파라미터는 2차식으로 만들고, 상수항은 없게 생성하겠다.

X_train_lstat_poly = poly.fit_transform(X_train_lstat) # X_train_lstat를 다항식으로 (train_set을 다항식 항으로)
X_test_lstat_poly = poly.fit_transform(X_test_lstat) # X_test_lstat를 다항식으로 (test_set을 다항식 항으로)

lin_reg.fit(X_train_lstat_poly, y_train) # 다항식 항으로 전처리 된 train_set으로 학습
print('다중 선형 회귀 LSTAT coefficients : ', lin_reg.coef_) # 다중 선형 회귀 LSTAT coefficients : [-2.22844813 0.03991878]
print('다중 선형 회귀 LSTAT intercept : ', lin_reg.intercept_) # 다중 선형 회귀 LSTAT intercept :  42.21995505402154

y_pred_lstat_poly = lin_reg.predict(X_test_lstat_poly) # 다항식으로 전처리 된 test_set으로 테스트
print(y_pred_lstat_poly[:5])

plt.scatter(X_test_lstat, y_test) # ~~~> 실제 값, 실제 값
# plt.polt(X_test_lstat, y_pred_lstat_poly) ~~~> 이렇게 그리면 2차함수의 모양이 나오지 않는다.(순서대로 x, y가 찍히지 않기 때문)

xs = np.linspace(X_test_lstat.min(), X_test_lstat.max(), 100).reshape((100, 1))
# X_test_lstat의 범위를 100개로 나누어 x 좌표 생성하고 100x1 2차원 리스트로
xs_poly = poly.fit_transform(xs)
# x 좌표들도 다항식으로 전처리
ys = lin_reg.predict(xs_poly)
# 전처리된 xs의 좌표로 새롭게 예측하고 그 값을 y 좌표로 생성
plt.plot(xs, ys, 'r')
# 이렇게 생성된 xs, ys로 예측 값 plot 그래프
# ~> 이렇게 생성하면 xs가 순서대로 정렬되고, ys 역시도 xs에 따라 정렬되므로 그래프가 올바르게 나온다.
plt.show()

# 변수 2개를 합친 price ~ RM + LSTAT  ----------------------------------------------------
# price ~ b0 + (b1 * RM) + (b2 * LSTAT)
X_train_rm_lstat = X_train[:, [5, 12]] # 'RM', 'LSTAT' 컬럼 사용.
X_test_rm_lstat = X_test[:, [5, 12]] # 변수를 2개 사용해 2차원 배열로 생성되기 때문에, 'np.newaxis'는 필요 없다.

lin_reg.fit(X_train_rm_lstat, y_train) # 'RM'과 'LSTAT'가 있는 train_set과 그 정답지로 학습
print('다중 선형 회귀 RM / LSTAT coefficients : ', lin_reg.coef_)
# 다중 선형 회귀 RM / LSTAT coefficients :  [ 5.0114298  -0.66908291]
print('다중 선형 회귀 RM / LSTAT intercept : ', lin_reg.intercept_)
# 다중 선형 회귀 RM / LSTAT intercept :  -0.6680381939230706

y_pred_rm_lstat = lin_reg.predict(X_test_rm_lstat) # 'RM'과 'LSTAT'가 있는 tset_set으로 테스트
print(y_test[:5], y_pred_rm_lstat[:5])

# 변수 2개를 합치고 다차항 형태 ----------------------------------------------------
# (1) Price ~ RM + LSTAT + RM^2 + RM*LSTAT + LSTAT2
# price = b0 + (b1 * rm) + (b2 * lstat) + (b3 * rm^2) + (b4 * rm * lstat) + (b5 * lstat^2)
X_train_rm_lstat_poly = poly.fit_transform(X_train_rm_lstat) # train_set을 다항식 항으로
X_test_rm_lstat_poly = poly.fit_transform(X_test_rm_lstat) # test_set을 다항식 항으로

lin_reg.fit(X_train_rm_lstat_poly, y_train) # 다항식으로 전처리 된 train_set으로 학습
print('다중 선형 회귀 다차항 RM / LSTAT coefficients : ', lin_reg.coef_)
# [-1.76285033e+01  1.52009093e+00  2.09295492e+00 -3.53889752e-01 -3.14275848e-03]
print('다중 선형 회귀 다차항 RM / LSTAT intercept : ', lin_reg.intercept_)
# 다중 선형 회귀 다차항 RM / LSTAT intercept :  58.131040227957655

y_pred_rm_lstat_poly = lin_reg.predict(X_test_rm_lstat_poly) # 다항식으로 전처리된 test_set으로 테스트
print(y_test[:5], y_pred_rm_lstat_poly[:5])

# (2) Price ~ RM + LSTAT + LSTAT^2
# price = b0 + (b1 * rm) + (b2 * lstat) + (b3 * lstat^2)
X_train_rm_lstat_2 = np.c_[X_train_rm, X_train_lstat_poly]  # 'RM'은 1차항, 'LSTAT'는 2차항이므로 LSTAT만 poly.
X_test_rm_lstat_2 = np.c_[X_test_rm, X_test_lstat_poly] # 그래서 np.c_로 '그냥 RM'과 'poly된 LSTAT'를 붙인다.

lin_reg.fit(X_train_rm_lstat_2, y_train)
print('다중 선형 회귀 다차항 RM / LSTAT 2 coefficients : ', lin_reg.coef_)
# 다중 선형 회귀 다차항 RM / LSTAT 2 coefficients :  [ 4.14148052 -1.79652146  0.03381396]
print('다중 선형 회귀 다차항 RM / LSTAT 2 intercept : ', lin_reg.intercept_)
# 다중 선형 회귀 다차항 RM / LSTAT 2 intercept :  11.976646227033507

y_pred_rm_lstat_2 = lin_reg.predict(X_test_rm_lstat_2)
print(y_test[:5], y_pred_rm_lstat_2[:5])

print('\n ------------------------------------------------------------------------------------------- \n')

# 5. Mean Square Error(MSE, 오차 제곱의 평균) 계산 ~> 실제값과 예측값을 전달

# error = y - y_hat, error^2 = (y - y_hat)^2 / MSE = sum(error^2) / 개수
print('단순 RM Mean Squared Error: ', mean_squared_error(y_test, y_pred_rm))
# 단순 RM Mean Squared Error:  49.422145607387066

print('단순 LSTAT Mean Squared Error: ', mean_squared_error(y_test, y_pred_lstat))
# 단순 LSTAT Mean Squared Error:  49.08238474704768

print('다중 LSTAT Mean Squared Error: ', mean_squared_error(y_test, y_pred_lstat_poly))
# 다중 LSTAT Mean Squared Error:  38.8530373167884

print('다중 LSTAT / RM Mean Squared Error: ', mean_squared_error(y_test, y_pred_rm_lstat))
# 다중 LSTAT / RM Mean Squared Error:  37.78636053598351

print('다중 POLY LSTAT / RM Mean Squared Error: ', mean_squared_error(y_test, y_pred_rm_lstat_poly))
# 다중 POLY LSTAT / RM Mean Squared Error:  32.661242648530354

print('다중 POLY LSTAT / RM 2 Mean Squared Error: ', mean_squared_error(y_test, y_pred_rm_lstat_2))
# 다중 POLY LSTAT / RM 2 Mean Squared Error:  31.2805735787169

# RMSE = sqrt(MSE)
print('단순 RM Squared Root Mean Squared Error: ', np.sqrt(mean_squared_error(y_test, y_pred_rm)))
# 단순 RM Squared Root Mean Squared Error:  7.030088591716826

print('단순 LSTAT Squared Root Mean Squared Error: ', np.sqrt(mean_squared_error(y_test, y_pred_lstat)))
# 단순 LSTAT Squared Root Mean Squared Error:  7.00588215337995

print('다중 LSTAT Squared Root Mean Squared Error: ', np.sqrt(mean_squared_error(y_test, y_pred_lstat_poly)))
# 다중 LSTAT Squared Root Mean Squared Error:  6.233220461109041

print('다중 LSTAT / RM Squared Root Mean Squared Error: ', np.sqrt(mean_squared_error(y_test, y_pred_rm_lstat)))
# 다중 LSTAT / RM Squared Root Mean Squared Error:  6.147061130002166

print('다중 POLY LSTAT / RM Squared Root Mean Squared Error: ', np.sqrt(mean_squared_error(y_test, y_pred_rm_lstat_poly)))
# 다중 POLY LSTAT / RM Squared Root Mean Squared Error:  5.715001544053191

print('다중 POLY LSTAT / RM 2 Squared Root Mean Squared Error: ', np.sqrt(mean_squared_error(y_test, y_pred_rm_lstat_2)))
# 다중 POLY LSTAT / RM 2 Squared Root Mean Squared Error:  5.592903859241363

print('\n ------------------------------------------------------------------------------------------- \n')

# 6. R2-score 계산 ~> 실제값과 예측값을 전달

r2_RM = r2_score(y_test, y_pred_rm)
print('단순 RM R2-score : ', r2_RM) # 단순 RM R2-score :  0.4407247091305826

r2_LSTAT = r2_score(y_test, y_pred_lstat)
print('단순 LSTAT R2-score : ', r2_LSTAT) # 단순 LSTAT R2-score :  0.44456954127327997

r2_LSTAT_2 = r2_score(y_test, y_pred_lstat_poly)
print('다중 LSTAT R2-score : ', r2_LSTAT_2) # 다중 LSTAT R2-score :  0.5603277947677918

r2_RM_LSTAT = r2_score(y_test, y_pred_rm_lstat)
print('다중 RM / LSTAT R2-score : ', r2_RM_LSTAT) # 다중 RM / LSTAT R2-score :  0.5723986176654351

r2_RM_LSTAT_poly = r2_score(y_test, y_pred_rm_lstat_poly)
print('다중 RM / LSTAT R2-score : ', r2_RM_LSTAT_poly) # 다중 RM / LSTAT R2-score :  0.6303959336867977

r2_RM_LSTAT_2 = r2_score(y_test, y_pred_rm_lstat_2)
print('다중 RM / LSTAT R2-score : ', r2_RM_LSTAT_2) # 다중 RM / LSTAT R2-score :  0.6460199841225782