import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scratch11_KNN.ex03_knn_직접구현 import train_test_split, MyScaler, MyKnnClassifier
from sklearn.metrics import confusion_matrix, classification_report

if __name__ == '__main__':
    # iris 데이터로 테스트 ================================================================
    # 데이터 세트 준비
    col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']
    iris = pd.read_csv('iris.csv', header=None, names=col_names)
    print(iris.iloc[:5])

    # 데이터 프레임을 이용해서 각 특성(변수)들과 Class(레이블)과의 관계를 그래프로 나타내기
    iris_by_class = iris.groupby('Class')
    for name, group in iris_by_class:
        plt.scatter(x=group['sepal_length'], y=group['sepal_width'], label=name)
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    plt.legend()
    plt.show()

    iris_by_class = iris.groupby('Class')
    for name, group in iris_by_class:
        plt.scatter(x=group['petal_length'], y=group['petal_width'], label=name)
    plt.xlabel('petal_length')
    plt.ylabel('petal_width')
    plt.legend()
    plt.show()

    # 데이터 세트를 points와 labels로 구분
    X = iris.iloc[:, :-1].to_numpy()  # points
    y = iris.iloc[:, 4].to_numpy()  # labels

    # 학습/검증(train/test) 세트로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Scaling
    scaler = MyScaler()  # 생성자 호출
    scaler.fit(X_train)  # 스케일링 하기 위한 평균과 표준 편차 계산
    X_train = scaler.transform(X_train)  # 데이터 변환
    X_test = scaler.transform(X_test)

    # k-NN 알고리즘 적용
    knn = MyKnnClassifier(n_neighbors=9)  # 분류기 객체 생성
    knn.fit(X_train, y_train)  # 학습
    y_pred = knn.predict(X_test)  # 예측
    print(np.mean(y_test == y_pred))  # 예측 결과 확인

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # 위스콘신 데이터로 테스트 ================================================================
    # 데이터 세트 준비
    wisc = pd.read_csv('wisc_bc_data.csv')
    print(wisc.head())

    # 데이터 세트를 points와 labels로 구분
    X = wisc.iloc[:, 2:].to_numpy()
    y = wisc.iloc[:, 1].to_numpy()

    # 학습/검증(train/test) 세트로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Scaling
    scaler = MyScaler()  # 생성자 호출
    scaler.fit(X_train)  # 스케일링 하기 위한 평균과 표준 편차 계산
    X_train = scaler.transform(X_train)  # 데이터 변환
    X_test = scaler.transform(X_test)

    # k-NN 알고리즘 적용
    knn = MyKnnClassifier(n_neighbors=9)  # 분류기 객체 생성
    knn.fit(X_train, y_train)  # 학습
    y_pred = knn.predict(X_test)  # 예측
    print(np.mean(y_test == y_pred))  # 예측 결과 확인

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))




