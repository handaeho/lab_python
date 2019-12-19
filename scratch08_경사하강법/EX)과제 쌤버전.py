"""
mpg.csv 파일을 읽고, 셩사 하강법을 사용해 선형 회귀식 찾기
cty = slope * displ + intercept
"""
import random
import matplotlib.pyplot as plt

from scratch04_벡터및행렬연산.ex01 import vector_mean
from scratch08_경사하강법.ex03 import gradient_step
from scratch08_경사하강법.ex04 import minibatches, linear_gradient

with open('mpg.csv', encoding='utf-8') as f:
    # 파일 사용(read, write)이 끝났을 때, close() 자동 호출
    f.readline() # 1번째 라인(컬럼 이름)을 읽고 버림
    # 한 줄씩 읽어서 그 줄의 앞뒤 공백들(줄바꿈, \n)을 제거하고, ','로 문자열을 분리해서 만든 리스트를 df에 저장
    df = [line.strip().split(sep=',') for line in f]
print(df[0:5])

# 배기량과 시내연비만 추출 -> 데이터 타입 숫자
displ = [float(row[3]) for row in df]
cty = [float(row[8]) for row in df]
displ_cty = [(d, c) for d, c in zip(displ, cty)]
print(displ_cty[0:5])

def mini_batch_gd(dataset, epochs, learning_rate=0.001, batch_size=1, shuffle=True):
    """
    미니 배치 경사 하강법(데이터 셋을 일정 크기로 샘플링해, 각 평균 gradient를 계산하고, theta를 계산해서
    다음 theta 계산에 이용하며 최종 theta를 찾음.

    :param dataset: 데이터 셋(x, y를 갖는)
    :param epochs: 반복할 횟수
    :param learning_rate: 학습률(= step)
    :param batch_size: 미니 배치 할 때, 샘플링 크기
    ('batch_size=1'이면 확률적 경사 하강법과 같다. 전체를 1개의 샘플로 묶는것이므로)
    :param shuffle: 데이터 셋 순서 섞기
    :return:
    """
    dataset = dataset.copy() # 원본 데이터를 복사해 사용
    theta = [random.randint(-10, 10), random.randint(-10, 10)] # 처음 theta를 랜덤하게 지정
    # 경사 하강법으로 찾고자 하는 직선의 기울기와, 절편의 초기값을 랜덤하게 지정
    print('theta 초기 값 : ', theta)
    for epoch in range(epochs): # epoch 횟수만큼 반복
        if shuffle:
            random.shuffle(dataset) # 데이터 셋의 순서를 무작위로 섞음
        mini_batch = minibatches(dataset, batch_size, shuffle) # ex04에서 만든 'minibatches()' 함수 사용
        for batch in mini_batch: # 미니 배치 크기만큼 반복
            gradients = [linear_gradient(x, y, theta) for x, y in batch]
            # 샘플링된 미니 배치들의 각 gradient를 계산하기 위해, ex04의 'linear_gradient()'함수 사용
            gradient = vector_mean(gradients)
            # 각 gradient의 평균을 계산하기 위해, ex04의 'vector_mean()' 함수 사용
            theta = gradient_step(theta, gradient, -learning_rate)
            # 계산된 gradient(샘플들의 각 gradient 평균)와 학습률(step)을 통해 theta룰 변경하기 위해,
            # ex03의 'gradient_step()' 함수 사용
    return theta # 변경되며 계산된 최종 theta 리턴


def linear_regreesion(x, theta):
    """ 선형 회귀 함수 f(x) = ax + b """
    slope, intercept = theta
    return slope * x + intercept # f(x) = ax + b

if __name__ == '__main__':
    print('=== stochastic(확률적) 경사 하강법 ===')
    theta_stochastic = mini_batch_gd(displ_cty, epochs=200, shuffle=False)
    print(theta_stochastic) # [-2.5735185509250753, 25.85438932562088] -> 기울기, y절편

    print('=== batch 경사 하강법 ===')
    theta_batch = mini_batch_gd(displ_cty, learning_rate=0.01, epochs=5000, batch_size=len(displ_cty),shuffle=True)
    print(theta_batch) # [-2.6123988924642165, 25.92062363815618] -> 기울기, y절편
    # 반복 횟수와 학습률을 키웠더니, 결과가 좋아짐(200번 ~> 5000번, 0.001 ~> 0.01)
    # 올바른 결과를 찾기 위해서는 학습률과 반복 횟수를 적절하게 조정해가며 찾아야 한다.

    print('=== mini - batch 경사 하강법 ===')
    theta_mini = mini_batch_gd(displ_cty, epochs=1000, learning_rate=0.01, batch_size=32, shuffle=True)
    print(theta_mini) # [-2.597623073172828, 25.97413741548699]

    # 그래프 그리기
    plt.scatter(displ, cty)
    ys_stochastic = [linear_regreesion(x, theta_stochastic) for x in displ]
    ys_batch = [linear_regreesion(x, theta_batch) for x in displ]
    ys_mini = [linear_regreesion(x, theta_mini) for x in displ]

    plt.plot(displ, ys_stochastic, color='red', label='Stochastic GD')
    plt.plot(displ, ys_batch, color='green', label='Batch GD')
    plt.plot(displ, ys_mini, color='yellow', label='Mini Batch GD')

    plt.xlabel('Displacement (cc)')
    plt.ylabel('Fuel Efficiency (mpg)')
    plt.title('Fuel Efficiency vs Displacement')
    plt.legend()
    plt.show()
