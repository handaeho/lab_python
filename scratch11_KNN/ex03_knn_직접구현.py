"""
sklearn의 함수들과 knn 모델을 직접 구현해 보자.
"""
from collections import Counter

import numpy as np


def train_test_split(X, y, test_size):
    """
    X : numpy.ndarray (크기는 n * m) ---> 포인트
    y : 원소의 개수가 n개인 1차원 배열 ---> 레이블
    test_size : test_set의 크기 (train_set와 test_set의 비율. 0.0 ~ 1.0 사이의 값)

    또한, len(X) == len(y)라고 가정
    """
    # X의 길이
    length = len(X)

    # 인덱스를 저장하는 배열
    indices = np.array([i for i in range(length)]) # X의 길이(행 수)의 범위 내의 원소를 갖는 1차원 배열(길이 5면 0 ~ 4 원소)
    print('Shuffle 전 = ', indices) # Shuffle 전 =  [0 1 2 3 4]

    # 인덱스를 랜덤하게 셔플
    np.random.shuffle(indices)
    print('Shuffle 후 = ', indices) # Shuffle 후 =  [0 3 1 2 4]

    # X를 test_size의 비율로 자름
    cut = int(length * (1 - test_size))

    # 비율에 맞게 수정된 train_set / test_set 생성
    X_train = X[indices[:cut]] # X의 indices를 cut까지만큼 행을 갖는 리스트로 X_train 생성(cut=4면 처음부터 4행까지)
    X_test = X[indices[cut:]] # X의 indices를 cut부터 끝까지만큼 행을 갖는 리스트로 X_test 생성(cut=4면 4행부터 끝까지)
    y_train = y[indices[:cut]] # y의 indices를 cut까지 만큼 행을 갖는 리스트로 y_train 생성
    y_test = y[indices[cut:]] # y의 indices를 cut부터 끝까지만큼의 행을 갖는 리스트로 y_test 생성

    return X_train, X_test, y_train, y_test


class MyScaler:
    def fit(self, X):
        """ x의 각 특성(컬럼)들의 평균 & 표준편차 저장 -> 평균과 표준편차는 '특성 별'로 구해져야 한다. """
        self.feature_means = np.mean(X, axis=0) # X의 컬럼 기준(axis=0) 평균 계산
        self.feature_stds = np.std(X, axis=0) # X의 컬럼 기준(axis=0) 표준편차 계산
        print('평균 : ', self.feature_means, '표준편차 : ', self.feature_stds)

    def transform(self, X):
        """ x의 평균을 0 / 표준편차를 1로 표준화하고 리턴 """
        dim = X.shape
        transformed = np.empty(dim) # X.shape는 X의 행과 열의 개수. 즉, X의 행과 열 수와 같은 비어있는 배열 생성.
        for row in range(dim[0]): # X의 행 수만큼 반복
            for col in range(dim[1]): # X의 열 수만큼 반복
                # x_new = (x - mean) / std
                transformed[row, col] = (X[row, col] - self.feature_means[col]) / self.feature_stds[col]
                # X의 1열 6, 8, 98, 4는 1열의 결과에 해당하는 평균 6.5와 표준편차 1.658로 표준화 하고,
                # X의 2열 7, 2, 9, 2는 2열의 결과에 해당하는 평균 5.0과 표준편차 3.082로 표준화 해야한다.
        return transformed

class MyKnnClassifier:
    def __init__(self, n_neighbors=5):  # 객체 생성
        """최근접 이웃으로 선택할 개수를 저장함."""
        self.k = n_neighbors

    def fit(self, X_train, y_label):  # 모델 훈련
        """레이블을 가지고 있는 데이터(point)를 저장함."""
        self.points = X_train
        self.labels = y_label

    def predict(self, X_test):  # 예측
        """테스트 세트 X_test의 각 점들마다,
        1) 학습 세트에 있는 모든 점들과의 거리를 계산.
        2) 계산된 거리들 중에서 가장 짧은 거리 k개를 선택.
        3) k개 선택된 레이블들 중에서 가장 많은 것(다수결)을 예측값으로 함."""
        predicts = []  # 예측값들을 저장할 리스트
        for test_pt in X_test:  # 테스트 세트에 있는 점들의 개수만큼 반복
            # 학습 세트의 점들과의 거리를 계산
            distances = self.distance(self.points, test_pt)
            print(test_pt)
            print(distances)
            # 다수결로 예측값 결정
            winner = self.majority_vote(distances)
            # 예측값을 리스트에 저장
            predicts.append(winner)

        return np.array(predicts)  # 예측값들의 배열을 리턴

    def distance(self, X, y):
        """점(벡터) y와 점(벡터)들 X 사이의 거리들의 배열을 리턴 """
        return np.sqrt(np.sum((X - y) ** 2, axis=1))

    def majority_vote(self, distances):
        # 거리 순서로 정렬된 인덱스를 찾는다.
        indices_by_distance = np.argsort(distances)
        print(indices_by_distance)
        # 가장 가까운 k개 이웃의 레이블을 찾는다.
        k_nearest_neighbor = []
        # for i in range(self.k):
        #     idx = indices_by_distance[i]
        #     k_nearest_neighbor.append(self.labels[idx])
        for i in indices_by_distance[0:self.k]:
            k_nearest_neighbor.append(self.labels[i])
        print(k_nearest_neighbor)
        # 가장 많은 득표를 얻은 레이블을 찾는다.
        vote_counts = Counter(k_nearest_neighbor)
        print(vote_counts)
        # most_common(n): 가장 많은 빈도수 순위 n까지의 리스트를 리턴
        # 빈도수가 동률일 수도 있기 때문에 리스트를 리턴
        print(vote_counts.most_common(1))
        print(vote_counts.most_common(1)[0])
        winner, winner_count = vote_counts.most_common(1)[0]
        return winner


if __name__ == '__main__':
    # 포인트 X 생성 --------------------
    np.random.seed(1210)
    X = np.random.randint(10, size=(5, 2)) # 10보다 작은 정수로 이루어진 5행 2열 2차원 배열
    print(X)
    # [[6 7]
    #  [8 9]
    #  [4 2]
    #  [8 2]
    #  [0 2]]

    # 레이블 y 생성 --------------------
    y = np.array(['a', 'b', 'a', 'b', 'a'])
    print(y)
    # ['a' 'b' 'a' 'b' 'a']

    # train_set / test_set 생성 --------------------
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    print(X_train)
    # [[6 7]
    #  [8 2]
    #  [8 9]
    #  [4 2]]
    print(y_train)
    # ['a' 'b' 'b' 'a']

    # 평균과 표준편차 계산 --------------------
    scaler = MyScaler() # MyScaler의 메소드를 사용하기 위해 MyScaler 객체 생성
    scaler.fit(X_train) # 평균 :  [6.5 5. ] 표준편차 :  [1.6583124 3.082207 ]

    # 표준화 --------------------
    X_train_scaled = scaler.transform(X_train)
    print(X_train_scaled)
    # [[-0.30151134  0.64888568]
    #  [ 0.90453403 -0.97332853]
    #  [ 0.90453403  1.29777137]
    #  [-1.50755672 -0.97332853]]

    X_test_scaled = scaler.transform(X_test)
    print(X_test_scaled)
    # [[-3.91964748 -0.97332853]]









