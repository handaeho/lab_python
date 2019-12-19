"""
편미분(Partial Differentiation)을 이용한 경사 하강법
"""
import random

from scratch04_벡터및행렬연산.ex01 import scalar_multiply, add, distance


def partial_difference_quotient(f, v, i, h=0.001):
    """
    '(f([x1, ..., xi + h, ..., xn]) - f([x1, ..., xi, ..., xn])) / h'를 구해 리턴

    :param f: 함수 f(vector) = float
    :param v: 기울기(gradient)를 계산할 점의 위치 -> vector(리스트 타입, [x1, ..., xn])
    :param i: 기울기를 계산 할 성분의 인덱스(정수, 몇번째 파라미터인가를 의미)
    :param h: i번째 성분의 변화량
    :return: 편미분의 결과 -> i번째 성분 방향의 기울기
    """
    # w = [v_j + (h if i == j else 0) for j, v_j in enumerate(v)] # 만약, i = 1면 1번째 원소에만 + h를 한다는 의미.
    # -> enumerate(리스트) : 리스트를 전달 받아, 리스트의 순서와 값을 리턴
    # 이를 아래와 같이 표현 할 수 있다.
    w = []
    for j, v_j in enumerate(v):
        if j == i:
            v_j += h
        w.append(v_j)

    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.001):
    """
    '[df/dx1, df/dx2, ..., df/dxi, ..., df/dxn]'를 구해 리턴

    :param f: 함수 f(vector) = float
    :param v: 기울기를 계산할 점의 위치 -> vector(리스트 타입, [x1, ..., xn])
    :param h: 증분(increment)
    :return: 모든 성분의 기울기들로 이루어진 vector(리스트)
    """
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]
    # ~~~> 함수 f의 v 위치에서 i번째 기울기


def gradient_step(v, gradient, step=-0.1):
    """
    [vi + step * df/dvi]

    :param v: 이동 전, 점들의 위치(리스트)
    :param gradient: 점 v에서의 기울기
    :param step: 이동하는 가중치(학습률)
    :return: gradient의 방향 or 반대방향으로 이동된 점들의 새로운 위치
    """
    # step * df/dxi
    increment = scalar_multiply(step, gradient) # scalar_multiply() ~> 리스트의 성분들에 같은 상수를 곱해줌.
    # xi + step * df/dxi
    return add(v, increment) # 여기서 add()는 벡터의 합을 계산하는 함수로, scratch04_벡터및행렬연산.ex01에서 우리가 만들었던 것.


def f(v):
    return v[0] ** 2 + v[1] ** 2 # 최소값 = (0, 0)

def g(v):
    return (v[0] - 1) ** 2 + (v[1] + 1) ** 2 # 최소값 = (1, -1)

if __name__ == '__main__':
    # f
    init_v = [random.randint(-10, 10) for i in range(2)]
    print(init_v)
    tolerance = 0.0000001
    count = 0
    while True:
        count += 1
        gradient = estimate_gradient(f, init_v, 0.001)
        next_v = gradient_step(init_v, gradient, -0.1)
        print(count, ':', next_v)

        if distance(next_v, init_v) < tolerance:
            # 이동 전, 후의 x값의 차이가 tolerance 미만이면 반복문 종료
            break
        else:
            # 이동한 점은 다음 반복 때는 시작 점이 됨.
            init_v = next_v
    # [-4, 4]
    # 1 : [-3.200100000000191, 3.1998999999992748]
    # 2 : [-2.5601800000001305, 2.559819999999476]
    # 3 : [-2.0482440000001176, 2.0477559999997084]
    # ...
    # 72 : [-0.0005004211965105285, -0.0004995786981771799]
    # 73 : [-0.0005003369572084228, -0.0004996629585417439]
    # 74 : [-0.0005002695657667382, -0.0004997303668333951]

    # g
    init_v = [random.randint(-10, 10) for i in range(2)]
    print(init_v)
    tolerance = 0.0000001
    count = 0
    while True:
        count += 1
        gradient = estimate_gradient(g, init_v, 0.001)
        next_v = gradient_step(init_v, gradient, -0.1)
        print(count, ':', next_v)

        if distance(next_v, init_v) < tolerance:
            # 이동 전, 후의 x값의 차이가 tolerance 미만이면 반복문 종료
            break
        else:
            # 이동한 점은 다음 반복 때는 시작 점이 됨.
            init_v = next_v
    # [-6, -6]
    # 1 : [-4.600099999998747, -5.000099999999236]
    # 2 : [-3.4801799999987395, -4.200179999999193]
    # 3 : [-2.584243999999586, -3.560243999999585]
    # ...
    # 74 : [0.9994995282346333, -1.0005003369656336]
    # 75 : [0.9994996225877066, -1.000500269572507]
    # 76 : [0.9994996980701654, -1.0005002156580056]



