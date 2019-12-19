"""
Linear Regression(선형 회귀) : 값을 '예측'하기 위한 알고리즘

Logistic Regression(로지스틱 회귀) : 값을 '분류'하기 위한 알고리즘
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split


# iris 데이터 셋 load
iris = load_iris()
X = iris.data
y = iris.target
features = iris['feature_names']

# np.ndarray 타입인 데이터 셋을 pandas.DataFrame으로
iris_df = pd.DataFrame(X, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
print(iris_df.iloc[:5, :])

# iris_df에 'species' 컬럼(target)을 추가
iris_df['species'] = y
print(iris_df.iloc[:5, :])
print(iris_df.describe())

# seaborn 패키지로 시각화
sns.pairplot(iris_df, hue='species', vars=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
plt.show()

# X(data), y(target)을 train_set / test_set으로 분할
X_trian, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1217) # ~> like random.seed(1217)

# Logistic Regression(로지스틱 회귀)을 사용하기 위한 객체 생성
log_reg = LogisticRegression()

# train_set으로 로지스틱 모델 fitting(훈련)
log_reg.fit(X_trian, y_train)

# 학습된 모델을 사용해 test_set을 분류 예측
predictions = log_reg.predict(X_test)
print('True = ', y_test)
print('predictions = ', predictions)

# 분류 결과를 평가하기 위한 confusion_matrix
print(confusion_matrix(y_test, predictions))

# 분류 결과를 평가하기 위한 classification_report
print(classification_report(y_test, predictions))



