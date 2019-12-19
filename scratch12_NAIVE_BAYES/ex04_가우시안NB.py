"""
'가우시안 Naive Bayes' 모델 - '연속형 자료'라면 '가우시안 모델 선택' 필요

연속형 변수에서의 Naive Bayes 원리
"""
from math import exp, pi, sqrt
from collections import defaultdict
from sklearn.datasets import load_iris

import random
import numpy as np
import pandas as pd



def separate_by_class(dataset):
    """
    dataset(리스트)를 class 별로 분류한 dict를 리턴
    {class_0: [[], [], [], ...],
    class_1: [[], [], [], ...]}
    """
    separated = dict() # 빈 dict 생성

    for i in range(len(dataset)): # dataset 크기만큼 반복
        vector = dataset[i] # dataset의 i번쨰 row, 전체 col 가져옴
        class_value = vector[-1] # vector의 가장 마지막 원소는 class(레이블)

        if class_value not in separated: # class_value가 separated dict에 없으면(dict의 키로 존재하지 않으면)
            separated[class_value] = [] # 값을 추가하기 위한 빈 리스트 생성

        separated[class_value].append(vector) # vector를 class_value값으로 추가

    return separated # 생성된 separated dict 리턴


def separate_by_class2(dataset):
    """
    separate_by_class 함수를 defaultdict 메소드를 사용해 더 간단하게
    """
    separated = defaultdict(list) # defaultdict 객체 생성
    for i in range(len(dataset)):
        vector = dataset[i]
        class_value = vector[-1]
        # 클래스를 key를 갖는 리스트에 vector 추가
        separated[class_value].append(vector) # 키 값이 있는지 없는지 체크를 할 필요가 없다.

    return separated


def summarize_dataset(dataset):
    """
    데이터 세트의 각 컬럼(변수, 특성)의 평균과 표준 편차들을 계산, 리턴
    [(mean, std, count), (), ...]
    """
    # for col in zip(*dataset):
    #     print(col)
    # *: unpacking 연산자
    #   *[1, 2] -> 1, 2
    #   *[[1,2], [3,4]] -> [1,2], [3,4]
    # zip(*[[1,2], [3,4]]) -> zip([1,2], [3,4]) -> [1, 3], [2, 4]
    summaries = [(np.mean(col), np.std(col), len(col))
                 for col in zip(*dataset)]

    del summaries[-1] # 마지막 컬럼은 데이터가 아니라 클래스(레이블)이므로 평균, 표준편차가 필요 없음

    return summaries


def summarize_by_class(dataset):
    """
    데이터 세트의 각 컬럼(특성, 변수)들에 대해서 각 클래스(레이블)별로 평균, 표준편차, 개수 계산
    {class_0: [(x1_mean, x1_std, x1_len), (x2_mean, x2_std, x2_len), ...],
    class_1: [(x1_mean, x1_std, x1_len), (x2_mean, x2_std, x2_len), ...], ...}
    """
    # 데이터 세트를 클래스 별로 분류
    separated = separate_by_class2(dataset)
    summaries = dict()
    # class_value를 key, vectors(각 컬럼(특성)별 평균, 표준편차)를 value로 dict에 저장
    for class_value, vectors in separated.items(): # key와 함께 value까지 꺼내야 하므로 .items() 필요
        summaries[class_value] = summarize_dataset(vectors)

    return summaries


def calculate_probability(x, mu, sigma):
    """ 가우시안 정규 분포 공식 계산 """
    exponent = exp(-((x-mu) ** 2) / (2 * sigma ** 2))

    return (1 / (sqrt(2 * pi) * sigma)) * exponent


def calculate_class_probability(summaries, vector):
    """
    주어진 vector의 각 클래스별 예측 값 계산
    Naive Bayes 정리 => P(class|x1, x2) ~ P(class) * P(x1|class) * P(x2|class)

    summaries : 클래스별로 분류 ---> dict 타입
    vector : 각 컬럼(특성)들의 평균, 표준편차 ---> list 타입
    """
    total_rows = sum([vector[0][2] for _, vector in summaries.items()])
    probabilities = dict() # 새로운 x1, x2에 대한 새로운 vector가 들어오기 때문에 dict 타입으로 생성
    for class_value, class_summaries in summaries.items(): # class_value에 key를, class_summaries에 value를
        # p = p(class)
        probabilities[class_value] = class_summaries[0][2] / total_rows
        # probabilities dict는 class_value를 key로, 원소를 total로 나누어 확률을 value로
        for i in range(len(class_summaries)):
            mu, sigma, count = class_summaries[i]
            # prob = P(x1|class)
            prob = calculate_probability(vector[i], mu, sigma)
            # p = P(class) * P(x1|class)
            probabilities[class_value] *= prob

    return probabilities


if __name__ == '__main__':
    # 테스트용 데이터 생성
    random.seed(1212)
    dataset = [[random.random(), random.random(), x // 5] for x in range(10)] # dataset = [[x1, x2, label], ...]
    print(dataset)

    df = pd.DataFrame(dataset, columns=['x1', 'x2', 'Class'])
    print(df)

    separated = separate_by_class(dataset)
    print(separated)

    separated2 = separate_by_class2(dataset)
    print(separated2)

    summary = summarize_dataset(dataset)
    print(summary)

    summaries = summarize_by_class(dataset)
    print(summaries)

    print(dataset[0]) # [0.7899567764583166, 0.29996159568611847, 0]
    probabilities = calculate_class_probability(summaries, dataset[0])
    print(probabilities) # {0: 0.642932959094217, 1: 0.011630975375924323}
    # 따라서 1번 데이터는 0번 클래스일 가능성이 높다.

    print(dataset[5])  # [0.05117528145254413, 0.4027997523802139, 1]
    probabilities = calculate_class_probability(summaries, dataset[5])
    print(probabilities)  # {0: 0.051753186984799276, 1: 0.6966316264471655}
    # 따라서 5번 데이터는 1번 클래스일 가능성이 높다.

    # iris 데이터에 적용
    # iris 데이터 load (from sklearn.datasets import load_iris)
    X, y = load_iris(return_X_y=True)
    # np.c_ : 두개의 리스트를 column 방향(세로)으로 묶기
    # np.r_ : 두개의 리스트를 row 방향(가로)로 묶기
    iris_dataset = np.c_[X, y]
    print(iris_dataset[:5])

    # iris_dataset[0], iris_dataset[50], iris_dataset[100] 데이터들이 속할 클래스 확률 계산
    summaries = summarize_by_class(iris_dataset)
    probabilities = calculate_class_probability(summaries, iris_dataset[0])
    print(probabilities) # {0.0: 2.894053528280388, 1.0: 3.929662157976779e-18, 2.0: 2.0584895837141273e-25}
    # 따라서 iris_dataset의 1번 데이터는 0번 클래스가 될 확률이 높다.

    probabilities = calculate_class_probability(summaries, iris_dataset[50])
    print(probabilities) # {0.0: 6.10015464109645e-111, 1.0: 0.015262048871741643, 2.0: 0.003719709397757642}
    # 따라서 iris_dataset의 50번 데이터는 1번 클래스가 될 확률이 높다.

    probabilities = calculate_class_probability(summaries, iris_dataset[100])
    print(probabilities) # {0.0: 7.641307394321016e-256, 1.0: 1.5021518865216958e-12, 2.0: 0.023641784333667433}
    # 따라서 iris_dataset의 100번 데이터는 2번 클래스가 될 확률이 높다.





