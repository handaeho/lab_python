"""
Scikit-learn 패키지를 이용한 Naive Bayes 알고리즘

- Bayes 정리 : 조건부 확률을 계산. A일 때 B일 확률 P(A|B) = P(A∩B) / P(B) = P(B|A)P(A) / P(B)
- Naive Bayes : 데이터 세트의 모든 변수들은 서로 독립적이라고 가정

Naive Bayes 분류기를 사용한 iris 품종 분류 및 예측
"""
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler


# 1. iris 데이터 세트(iris) load
iris = datasets.load_iris() # 'scikit-learn'에는 'iris' 데이터 세트를 포함한 여러 데이터 세트가 내장되어 있다.
print(type(iris)) # <class 'sklearn.utils.Bunch'>
# ---> Bunch : dict의 {key:value} 형태와 비슷하게 {'data': [], 'target': []}을 갖는 클래스.
#      data : 특성(변수). n차원상의 점(points) / target : label(분류 클래스)

# 2. 데이터 확인
print('data = ', iris.data.shape)
# data =  (150, 4)
print('iris target = ', iris.target_names)
# iris target =  ['setosa' 'versicolor' 'virginica']
print('iris feature = ', iris.feature_names)
# iris feature =  ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

# 3. 포인트 X(data)와 레이블 y(target) 설정
X = iris.data
print('type X : ', type(X)) # type X :  <class 'numpy.ndarray'>
print(X[:5])
y = iris.target
print('type y : ', type(y)) # type y :  <class 'numpy.ndarray'>
print(y[:5])

# 이 내용을 load할 때, 설정할 수도 있다.
X, y = datasets.load_iris(return_X_y=True)
# 'retuen X_y=True'로 설정하면 numpy.ndarray들의 tuple(data, target)을 리턴
# 'retuen X_y=False(기본값)'로 설정하면, Bunch 클래스 타입을 리턴

# 4. 데이터 셋을 train_set / test_set로 나눔
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 5. 데이터 변환(스케일링. 표준화 또는 정규화)
scaler = StandardScaler() # 생성자 호출 - 변환기(StandardScaler) 객체 생성
scaler.fit(X_train, y_train) # 학습 데이터와 학습레이블의 평균과 표준편차를 스케일링 하기 위해서
X_train_transformed = scaler.transform(X_train) # 학습 데이터의 평균과 표준편차 스케일링
X_test_transformed = scaler.transform(X_test) # 테스트 데이터의 평균과 표준편차 스케일링

# 6. 모델 선택 및 학습
gnb = GaussianNB() # '가우시안 Naive Bayes' 모델 객체 생성 - '연속형 자료'라면 '가우시안 모델 선택' 필요
gnb.fit(X_train_transformed, y_train) # 모델 학습
y_pred = gnb.predict(X_test_transformed) # 예측 (X_test_transformed는 정답지 역할)

# 7. 모델 평가 - Confusion Matrix
print(confusion_matrix(y_test, y_pred)) # (실제값, 예측값)
# [[12  0  0]
#  [ 0  9  1]
#  [ 0  0  8]]
print(classification_report(y_test, y_pred)) # (실제값, 예측값)


