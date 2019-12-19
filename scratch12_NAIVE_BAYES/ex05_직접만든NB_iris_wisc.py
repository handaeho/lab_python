"""
'iris 데이터'와 '위스콘신 암 데이터'를 직접 구현한 Navie Bayes 모델로 분류 및 예측
"""
import os
import numpy as np
import pandas as pd

from scratch12_NAIVE_BAYES.ex04_가우시안NB import separate_by_class2, summarize_dataset, \
    summarize_by_class, calculate_class_probability


def train_test_split(df, test_size):
    """
    df : DataFrame
    test_size : train_set와 test_set의 비율
    학습 set(X_train)와 검증 set(X_test)을 리스트 타입으로 리턴
    """
    length = len(df)
    indices = np.array([i for i in range(length)]) # df의 길이만큼 원소를 갖는 리스트
    np.random.shuffle(indices) # 랜덤하게 train_set과 test_set를 구성하기 위해 셔플
    cut = int(length * (1 - test_size)) # 테스트 사이즈만큼 나누기 위함

    X_train = df[indices[:cut]]
    X_test = df[indices[cut:]]

    return X_train, X_test


def predict(summaries, X_test):
    """
    테스트 세트의 예측값들의 리스트를 리턴
    """
    pred = []
    for vector in X_test:
        prob = calculate_class_probability(summaries, vector)
        pred.append(max(prob, key= lambda key: prob[key]))

    return pred


if __name__ == '__main__':
    # 1. csv 파일 경로 설정
    iris_file = os.path.join('..', 'scratch11_KNN', 'iris.csv')
    cancer_file = os.path.join('..', 'scratch11_KNN', 'wisc_bc_data.csv')

    # 2. csv 파일 load
    col_names = ['sepal-lenght', 'sepal-width', 'petal-length', 'petal-width', 'Class']
    iris_dataset = pd.read_csv(iris_file, header=None, names=col_names)
    cancer_dataset = pd.read_csv(cancer_file)

    # 3. 데이터 전처리
    # cancer_dataset의 id 컬럼을 지우고 diagnosis 컬럼을 맨뒤로 보내야 한다.
    # iris_dataset과 cancer_dataset의 class를 숫자로 표현 해야한다.

    # 3-1) cancer dataset의 id 컬럼 제거.
    cancer_dataset = cancer_dataset.iloc[:, 1:]
    print(cancer_dataset)

    # DataFrame.drop(columns=['컬럼명'])을 사용해도 된다.
    # cancer_dataset_ret = cancer_dataset.drop(columns=['id'])
    # print(cancer_dataset_ret)

    # 3-2) cancer dataset의 diagnosis 컬럼을 맨 뒤로
    cancer_cols = cancer_dataset.columns.tolist() # cancer_dataset 컬럼명을 리스트로
    print(cancer_cols)
    cancer_cols = cancer_cols[1:] + cancer_cols[:1] # 1번 컬럼을 맨 뒤로
    cancer_dataset = pd.DataFrame(cancer_dataset, columns=cancer_cols) # 순서를 바꾼 컬럼명으로 다시 데이터프레임 생성
    print(cancer_dataset)

    # 3-3) class를 숫자 형식으로
    iris_class = iris_dataset.iloc[:, 4]
    for i in range(len(iris_dataset)):
        if iris_class[i] == 'Iris-setosa':
            iris_class[i] = 0
        elif iris_class[i] == 'Iris-versicolor':
            iris_class[i] = 1
        elif iris_class[i] == 'Iris-virginica':
            iris_class[i] = 2
    print(iris_class)
    print(iris_dataset.head())

    cancer_class = cancer_dataset.iloc[:, -1]
    print(cancer_class)
    for i in range(len(cancer_dataset)):
        if cancer_class[i] == 'B':
            cancer_class[i] = 0
        elif cancer_class[i] == 'M':
            cancer_class[i] = 1
    print(cancer_dataset.head())

    # 3-4) 데이터프레임을 ndarray로
    iris_dataset = iris_dataset.to_numpy()
    cancer_dataset = cancer_dataset.to_numpy()
    print(iris_dataset)
    print(cancer_dataset)

    # 4. train_set / test_set으로 분할
    iris_X_train, iris_X_test = train_test_split(iris_dataset, test_size=0.2)
    cancer_X_train, cancer_X_test = train_test_split(cancer_dataset, test_size=0.2)
    print(iris_X_train.shape) # (120, 5)
    print(iris_X_test.shape) # (30, 5)
    print(cancer_X_train.shape) # (455, 31)
    print(cancer_X_test.shape) # (114, 31)


    # 5. 직접 만든 Naive Bayes 함수에 적용

    # 5-1) 리스트를 클래스별로 분류한 dict 생성
    iris_separated = separate_by_class2(iris_dataset)
    print(iris_separated)
    cancer_separated = separate_by_class2(cancer_dataset)
    print(cancer_separated)

    # 5-2) 데이터 셋의 각 컬럼(특성)별 평균과 표준편차 계산
    iris_summary = summarize_dataset(iris_dataset)
    print(iris_summary)
    cancer_summary = summarize_dataset(cancer_dataset)
    print(cancer_summary)

    # 5-3) 데이터 셋의 각 컬럼(특성)에 대해 각 클래스(레이블)별로 평균, 표준편차, 개수 계산
    iris_summaries = summarize_by_class(iris_dataset)
    print(iris_summaries)
    cancer_summaries = summarize_by_class(cancer_dataset)
    print(cancer_summaries)

    # 6. 예측
    iris_pred = predict(iris_summaries, iris_X_test)
    print(iris_pred) # [2, 0, 1, 0, 2, 2, 2, 1, 0, 2, 1, 2, 0, 1, ...]
    cancer_pred = predict(cancer_summaries, cancer_X_test)
    print(cancer_pred) # [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, ...]


