"""
Scikit-learn 패키지를 이용한 Naive Bayes 알고리즘

Naive Bayes 분류기를 사용한 위스콘신 암 데이터 분류 및 예측
"""
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler


# 1. wisc 데이터 세트(breast_cancer) load
wisc = datasets.load_breast_cancer()

# 2. 데이터 확인
print('data = ', wisc.data.shape)
# data =  (569, 30)
print('wisc target = ', wisc.target_names)
# wisc target =  ['malignant' 'benign']
print('wisc feature = ', wisc.feature_names)
# wisc feature =  ['mean radius' 'mean texture' 'mean perimeter' 'mean area' ... ]

# 3. 포인트 X(data)와 레이블 y(target) 설정
X = wisc.data
print('type X : ', type(X)) # type X :  <class 'numpy.ndarray'>
print(X[:5])
y = wisc.target
print('type y : ', type(y)) # type y :  <class 'numpy.ndarray'>
print(y[:5])

# 4. 데이터 셋을 train_set / test_set로 나눔
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 5. 데이터 변환(스케일링. 표준화 또는 정규화)
scaler = StandardScaler()
scaler.fit(X_train, y_train)
X_train_transformed = scaler.transform(X_train)
X_test_transformed = scaler.transform(X_test)

# 6. 모델 선택 및 학습
gnb = GaussianNB()
gnb.fit(X_train_transformed, y_train)
y_pred = gnb.predict(X_test_transformed)

# 7. 모델 평가 - Confusion Matrix
print(confusion_matrix(y_test, y_pred))
# [[34  7]
#  [ 7 66]]
print(classification_report(y_test, y_pred))

