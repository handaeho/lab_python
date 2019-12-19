"""
R을 활용한 머신러닝에서 사용한 '위스콘신 대학교의 암 데이터'에 대한, scikit-learn 패키지 활용
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


if __name__ == '__main__':
    # 1. csv 파일을 DataFrame으로
    dataset = pd.read_csv('wisc_bc_data.csv')
    print(dataset.info())
    print(dataset.describe())
    print(dataset.head())

    # 2. 데이터를 데이터(포인트)와 레이블로 구분
    X = dataset.iloc[:, 2:].to_numpy()
    Y = dataset.iloc[:, 1].to_numpy()

    # 3. train set 8 / test set 2 구성
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # 4. z-score 표준화
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    for col in range(len(dataset.iloc[0]) - 2):
        print(f' X_train 평균 = {X_train[:, col].mean()} / X_train 표준편차 = {X_train[:, col].std()}')
        print(f'X_test 평균 = {X_test[:, col].mean()} / X_test 표준편차 = {X_test[:, col].std()}')

    # 5. k-nn 분류기 생성
    classifier = KNeighborsClassifier(n_neighbors=5) # k 값은 5

    # 6. 분류기 학습
    classifier.fit(X_train, Y_train)

    # 7. 학습한 분류기로 예측
    y_pred = classifier.predict(X_test)
    print(y_pred)

    # 8. 모델 평가 - 혼동 행렬
    conf_matrix = confusion_matrix(Y_test, y_pred)
    print(conf_matrix)
    # [[73  1]
    # [ 0 40]]

    # 9. 상세 결과 분석
    report = classification_report(Y_test, y_pred)
    print(report)

    # 10. 모델 성능 개선 위한 k값 변화(평균 오차율 분석)
    errors = []
    for i in range(1, 41):
        knn = KNeighborsClassifier(n_neighbors=i)  # krkqtdmf 1 ~ 30까지 변화 시킴
        knn.fit(X_train, Y_train)
        pred_i = knn.predict(X_test)
        errors.append(np.mean(pred_i != Y_test))  # 예측값(pred_i)과 실제값(Y_test)이 다른 결과의 평균들을 errors 배열에 추가
    print(errors)

    # 11. k 값 변화에 따른 평균오차율 시각화
    plt.plot(range(1, 41), errors, marker='o')
    plt.title('Mean Error with K-Value')
    plt.xlabel('k-value')
    plt.ylabel('mean error')
    plt.show()


