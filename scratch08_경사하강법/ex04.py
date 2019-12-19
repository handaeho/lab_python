"""
선형 회귀(Linear Regression)
모델 y = ax + b에서, 기울기(slope) a와 y절편 b를 찾는 문제.

(a, b)를 특정 값으로 가정했을 때의 예상값과 실제값 사이의 오차들의 제곱의 합을 최소로 하는 파라미터 a와 b를 찾는 문제
- 실제값: (x, y)
- 예상값: y_hat = theta1 * x + theta2
- 오차: e = y_hat - y = theta1 * x + theta2 - y
- 오차 제곱: f = e**2 = (theta1 * x + theta2 - y)**2
- 기울기 theta1에 대한 편미분: df/dt1 ~ e * x
- y절편 theta2에 대한 편미분: df/dt2 ~ e

1) 확률적 경사 하강법(Stochastic Gradient Descent)
    = 전체 데이터 세트(훈련 세트)에서 샘플 데이터 1개씩 gradient를 계산. 파라미터(기울기, 절편) 변경.
    위 과정을 임의의 회수(epoch)만큼 반복

    (a1, b1)의 theta를 계산해, (a2, b2)에 적용해 계산하고, 다시 계산된 theta를 이용해 (a3, b3)을 계산하고, ...

2) 배치 경사 하강법(Batch GD)
    = 전체 데이터 세트를 사용해서 전체 gradient들의 평균을 gradient로 사용해서 파라미터 theta를 변경.
    위 과정을 임의의 회수(epoch)만큼 반복

    dataset의 모든 점들을 똑같은 theta를 사용해, gradient를 계산하고, 이 gradient의 평균을 계산한다.
    그래서 이 평균 gradient를 사용해서, theta를 변경한다.

3) 미니 배치 경사 하강법(Mini-batch GD)
    = 전체 데이터 세트를 크기를 작게 샘플링해서 처리하는 방식.
    각각의 epoch마다 데이터 세트의 순서를 섞어서 파라미터(theta)의 최적값을 찾음.

    확률적 경사 하강법과 배치 경사 하강법의 절충안.
    dataset를 일정 크기(batch_size)로 작게 샘플링하고, 그 샘플마다의 평균 gradient를 계산한다.(여기는 배치 경사와 비슷)
    그리고 1번째 샘플들의 gradient로 1번째 theta를 계산해서, 2번째 샘플들의 gradient로 2번째 theta를 계산하고,
    다시 2번째 theta로 3번째 샘플의 gradient를 계산하고, ... (여기는 확률적 경사와 비슷)
"""
import random

from scratch04_벡터및행렬연산.ex01 import vector_mean
from scratch08_경사하강법.ex03 import gradient_step


def linear_gradient(x, y, theta):
    """
    특정 데이터 (x, y)에서 기울기와 y절편에 대한 편미분 벡터 리턴

    :param x: 실제 데이터
    :param y: 실제 데이터
    :param theta: [theta1, theta2] 벡터(리스트). [기울기, y절편]
    """
    slope, intersect = theta
    y_hat = slope * x + intersect  # 예상값
    error = y_hat - y  # 오차
    # error**2을 최소화하는 slope(기울기), intersect(절편) 찾기
    # 점(x,y)에서 [기울기에 대한 편미분, 절편에 대한 편미분]
    gradient = [error * x, error]
    return gradient


def minibatches(dataset, batch_size, shuffle=True):
    # dataset를 무작위로 섞음
    if shuffle:
        random.shuffle(dataset)

    # 배치 시작 인덱스 : 0, batch_size, 2*batch_size, ...
    batch_starts = [s for s in range(0, len(dataset), batch_size)]
    mini = [dataset[s:s+batch_size] for s in batch_starts]
    # ~~~> batch_size가 20으로 전달받으면 dataset의 0 ~ 19번째까지 리스트를 만들고, 그 다음에는 20 ~ 39까지, ...
    # 데이터 세트를 작게 쪼개 생성

    return mini

dataset = [(x, 20 * x + 5) for x in range(-50, 51)]  # (x, y)가 튜플의 형태인 f(x) = 20x + 5 직선 위의 점 리스트


if __name__ == '__main__':
    print('=== 확률적 경사 하강법 ===')
    theta = [1, 1]  # [기울기, 절편], y = x + 1
    step = 0.001  # 파라미터의 값을 변경 할 때 사용할 가중치(학습률)

    for epoch in range(200):  # 임의의 횟수(epoch)만큼 반복
        random.shuffle(dataset)  # dataset을 랜덤하게 섞음
        # 각각의 epoch마다 dataset에서 샘플(x, y)를 추출.
        for x, y in dataset:
            # 각 점에서 gradient 계산
            gradient = linear_gradient(x, y, theta)
            # 파라미터 theta(기울기, 절편)를 변경
            theta = gradient_step(theta, gradient, -step)  # 최소화 문제이므로 step는 '-'

        if (epoch + 1) % 10 == 0:  # 10번마다 출력해보자.
            print(f'{epoch} : {theta}')
    # === 확률적 경사 하강법 ===
    # 9 : [19.94593591252035, 3.639652843491321]
    # ...
    # 199 : [20.0000000001283, 4.999999995485546] ~~~> (20, 5)를 근사하게 찾음.


    print('\n=== 배치 경사 하강법 ===')
    step = 0.001 # 학습률
    theta = [1, 1]  # 임의의 값으로 [기울기, 절편] 설정
    for epoch in range(5000):
        # 모든 샘플에서의 gradient를 계산
        gradients = [linear_gradient(x, y, theta) for x, y in dataset]
        # gradients의 평균을 계산
        gradient = vector_mean(gradients)
        # 파라미터 theta(기울기, 절편)을 변경
        theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 100 == 0:
            print(f'{epoch}: {theta}')
    # === 배치 경사 하강법 ===
    # 99: [20.0, 1.3808314115451645]
    # 199: [20.0, 1.7254046820854578]
    # 299: [20.0, 2.037171871375603]
    # ...
    # 4899: [20.0, 4.970286603475481]
    # 4999: [20.0, 4.973115552160543]


    print(' \n === 미니 배치 하강법 ===')
    step = 0.001 # 학습률
    theta = [1, 1] # 임의의 파라미터 시작 값
    for epoch in range(1000):
        mini_batchs = minibatches(dataset, 20, True)
        for batch in mini_batchs:
            gradients = [linear_gradient(x, y, theta) for x, y in batch]
            gradient = vector_mean(gradients)
            theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 100 == 0:
            print(f'{epoch} : {theta}')
    # === 미니 배치 하강법 ===
    # 99 : [19.904265231429196, 2.855299433806202]
    # 199 : [19.94155669476755, 3.8317290693196355]
    # 299 : [19.978528656354406, 4.360444238319913]
    # ...
    # 899 : [19.999189014021855, 4.983065755678633]
    # 999 : [20.00014487460703, 4.990799140706061]






