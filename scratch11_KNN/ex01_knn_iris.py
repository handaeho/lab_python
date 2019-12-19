"""
Scikit-learn 패키지를 이용한 k-nn(k-Nearest Neighbor, 최근접 이웃)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report


if __name__ == '__main__':
    # 1. 데이터 준비 ----------------------------------------------------------------------
    # csv 파일에 컬럼 이름(헤더 정보)들이 없기 때문에 컬럼 이름 부여
    col_names = ['sepal-lenght', 'sepal-width', 'petal-length', 'petal-width', 'Class']

    # 2. csv 파일에서 DataFrame 생성 ----------------------------------------------------------------------
    dataset = pd.read_csv('iris.csv', header=None, names=col_names)

    # 3. 'dataset' DataFrame 확인 ----------------------------------------------------------------------
    print(dataset.shape) # ~> (row 개수, column 개수)
    print(dataset.info()) # ~> 데이터 타입, row 개수, column 개수, column 데이터 타입
    print(dataset.describe()) # ~> 요약 통계 정보
    print(dataset.head())
    print(dataset.tail())
    print(dataset.iloc[ :5]) # = dataset.head()
    print(dataset.iloc[-5: ]) # = dataset.tail()
    print(dataset.iloc[0:5]) # 0 ~ 4행 출력 (행 인덱스를 사용하므로)
    print(dataset.loc[0:5]) # 0 ~ 5행 출력 (행 번호를 시용하므로)

    # 4. 데이터 전처리 ----------------------------------------------------------------------
    # 4-1) 데이터를 데이터(포인트)와 레이블로 구분
    X = dataset.iloc[:, : -1].to_numpy() # X = '전체 row'과 '0 ~ n-1(마지막만 제외) column' 선택 ---> n차원 상의 포인트
    Y = dataset.iloc[:, 4].to_numpy() # Y = '전체 row'와 '4번째(마지막) column' 선텍 ---> 레이블
    # ~~~> to_numpy() : DataFrame을 np.ndarray로 변환

    # 4-2) '전체 data set'를  'train set(학습 세트)' / 'test set(검증 세트)'로 나눔
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    # ~> X, Y를  X_train, X_test, Y_train, Y_test로, 각각 train 8 : test 2 비율로 나눈다.
    print(len(X_train), len(Y_train)) # 120 120
    print(len(X_test), len(Y_test)) # 30 30
    print(X_train[0:3])
    print(Y_train[0:3])

    # 4-3) 포인트들의 거리 계산을 위해서 각 특성들(각 변수들)을 스케일링(표준화)
    # ---> 'Z-Score 표준화' : 평균 = 0, 표준 편차 = 1로 변환
    scaler = StandardScaler() # scaler 객체 생성 (StandardScaler 모듈의 기능을 사용하기 위함)
    scaler.fit(X_train) # 표준화를 위해 X_train의 평균 & 표준편차 계산
    X_train = scaler.transform(X_train) # X_train에 대한 z-score 표준화 실행
    X_test = scaler.transform(X_test) # X_test에 대한 z-score 표준화 실행
    for col in range(4): # 표준화 수행 결과 확인
        print(f' X_train 평균 = {X_train[:, col].mean()} / X_train 표준편차 = {X_train[:, col].std()}')
        print(f'X_test 평균 = {X_test[:, col].mean()} / X_test 표준편차 = {X_test[:, col].std()}')

    # 5. 학습 & 예측 ----------------------------------------------------------------------
    # 5-1) k-nn 분류기 생성
    classifier = KNeighborsClassifier(n_neighbors=5) # n_neighbors = k 값

    # 5-2) 분류기 학습
    classifier.fit(X_train, Y_train)

    # 5-3) 학습된 분류기로 예측
    y_pred = classifier.predict(X_test)
    print(y_pred)

    # 6. 모델 평가 - Confusion Matrix(혼동 행렬) ----------------------------------------------------------------------
    conf_matrix = confusion_matrix(Y_test, y_pred) # confusion_matrix(y_true, y_pred)
    print(conf_matrix)
    # [[11  0  0]
    #  [ 0  7  1]
    #  [ 0  1 10]] ---> 대각선의 값(11, 7, 10)이 정확한 예측

    # 각 항목의 실제 값과 예측 값에 대한 상세 결과 출력
    report = classification_report(Y_test, y_pred)
    print(report)
    # precision : 정밀도 (양성으로 분류된 결과의 정확도. (TP + TN) / (TP + FP + FN + TN))
    # recall : 재현율 (실제 양성 모델이 정확하게 양성으로 예측한 비율. TP / (TP + FP))
    # f1-score : precision(정밀도)와 recall(재현율)의 조화평균(항상 정밀도와 재현율 사이의 값. TP / (TP + FN))
    #            (조화평균 - 주어진 값들의 역수의 산술 평균(일반적인 평균)의 역수)
    # 양성
    #   - TP(진양성) : 실제로 Ture일 때, True로 예측
    #   - FP(가양성) : 실제는 False일 때, True로 예측
    # 음성
    #   - TN(진음성) : 실제로 False일 때, False로 예측
    #   - FN(가음성) : 실제는 True일 때, False로 예측

    # 7. 성능 개선(모델 향상) - 'k' 값의 변화에 따른 결과 비교 --------------------------------------------------------
    errors = []
    for i in range(1, 41):
        knn = KNeighborsClassifier(n_neighbors=i) # k값을 1 ~ 30까지 변화시킴
        knn.fit(X_train, Y_train)
        pred_i = knn.predict(X_test)
        errors.append(np.mean(pred_i != Y_test)) # 예측값(pred_i)과 실제값(Y_test)이 다른 결과의 평균들을 errors 배열에 추가
    print(errors) # 평균에러. [0.0, 0.13333333333333333, 0.03333333333333333, 0.06666666666666667, 0.0, ...]

    # k 값의 변화에 따른 평균 에러율 시각화
    plt.plot(range(1, 41), errors, marker='o')
    plt.title('Mean Error with K-Value')
    plt.xlabel('k-value')
    plt.ylabel('mean error')
    plt.show()

