"""
Gradient Descent(경사 하강법)
= 최적화 문제(특정 상황에서 가장 적합한 모델을 찾는 문제)
    ex) 모델의 '오류'를 '최소화' / 'liklihood(우도)를 '최대화'
타겟 함수를 최소 or 최대로 만드는 파라미터를 찾는 문제

어떤 곡선의 접선을 찾아, 그 접선의 기울기 방향으로 이동하며 최소(또는 최대)값을 찾는다.

함수 f(x)의 기울기 : f'(x) = lim(h -> 0) 일 때, (f(x+h) - f(x)) / ((x+h) - x)
이때, h를 조절해 가며 최적의 기울기를 찾는다.

만약, '최소 값'을 찾고자 한다면 '기울기의 반대 방향'으로,
'최대 값'을 찾고자 한다면 '기울기의 방향'으로 움직여 가며 찾는다.
"""
import random

import matplotlib.pyplot as plt


def f(x):
    """
    함수 f(x) = x ** 2
    """
    return x ** 2


def f_derivative(x):
    """
    함수 f(x) = x ** 2의 도함수인 f'(x) = 2x
    """
    return 2 * x


def tangent(x, a, x1, y1):
    """
    (x1, y1)을 지나는 기울기 a인 직선의 방정식 y = a(x - x1) + y1

    :param x:
    :param a: 기울기
    :param x1: x 좌표
    :param y1: y 좌표
    :return: 직선의 방정식
    """
    return a * (x - x1) + y1


def difference_quotient(f, x, h):
    """
    함수 f(x)의 기울기인 f'(x) = lim(h -> 0) 일 때, (f(x+h) - f(x)) / ((x+h) - x)를 리턴
    즉, f'(x)의 근사값
    """
    return (f(x + h) - f(x)) / h


def move(x, direction, step=-0.1):
    """
    x 좌표를 새로운 x로 이동.
    step < 0이면, '접선과 같은 방향'으로, ~~~> '최소값 찾기'
    step > 0이면, '접선과 반대 방향'으로 이동. ~~~> '최대값 찾기'

    direction -> 접선의 기울기
    """
    return x + step * direction

if __name__ == '__main__':
    # 그래프의 x 좌표들(구간 -3.0, -2.9, ..., 2.9, 3.0)
    xs = [x / 10 for x in range(-30, 31)]
    # 그래프의 y 좌표들
    ys = [f(x) for x in xs]

    # f(x) = x ** 2에서 x = -1의 접선 y = ax + b(기울기 a, y 절편 b)
    # 기울기 a는 f'(x)로,
    # y 절편 b는 f(x)가 x = x1 좌표를 지날 때, (x1, f(x1))을 지나는 직선임을 이용해 찾음.
    a = f_derivative(-1)  # x = -1에서 접선의 기울기 a
    x1, y1 = -1, f(-1)  # x = -1에서 곡선과 접선이 만나는 점의 좌표
    tangents = [tangent(x, a, x1, y1) for x in xs]

    # f'(x)의 근사값을 사용해, x = -1에서 기울기 a2를 찾음
    h1 = 1
    a2 = difference_quotient(f, x=-1, h=h1)
    tangent_estimates_1 = [tangent(x, a2, x1, y1) for x in xs]

    # 그럼 h를 줄여보자.
    h2 = 0.5
    a2 = difference_quotient(f, x=-1, h=h2)
    tangent_estimates_0_5 = [tangent(x, a2, x1, y1) for x in xs]

    h3 = 0.1
    a2 = difference_quotient(f, x=-1, h=h3)
    tangent_estimates_0_1 = [tangent(x, a2, x1, y1) for x in xs]

    # ~~~> h 값이 감소하며 '0'에 수렴 할 수록, actual 접선에 가까워 지고 있다.

    plt.plot(xs, ys)

    plt.plot(xs, tangents, label='actual')
    plt.plot(xs, tangent_estimates_1, label=f'estimate : h = {h1}')
    plt.plot(xs, tangent_estimates_0_5, label=f'estimate : h = {h2}')
    plt.plot(xs, tangent_estimates_0_1, label=f'estimate : h = {h3}')

    plt.ylim(bottom=-3)
    plt.axhline(y=0, color='black') # y=0인 수평 보조선
    plt.axvline(x=0, color='black') # x=0인 수직 보조선
    plt.legend()
    plt.show()

    # 실제 기울기(f_derivative)와 기울기 근사값(difference_quotient)의 비교
    xs = [x for x in range(-10, 11)]
    actuals = [f_derivative(x) for x in xs] # xs의 구간에서 모든 기울기

    estimates_1 = [difference_quotient(f, x, h=1) for x in xs] # h=1일 때, 기울기 근사값
    estimates_2 = [difference_quotient(f, x, h=0.1) for x in xs] # h=0.1일 때, 기울기 근사값

    plt.scatter(xs, actuals, label='actual', marker='x')
    plt.scatter(xs, estimates_1, label='h = 1', marker='+')
    plt.scatter(xs, estimates_2, label='h = 0.1', marker='o')
    # ~~~> h가 0에 수렴 할 수록, actual 기울기와 가까워진다.

    plt.legend()
    plt.show()

    # Gradient Descent(경사 하강법)
    xs = [x / 10 for x in range(-30, 31)] # x : -3.0, -2.9, ..., 2.9, 3.0
    ys = [f(x) for x in xs] # f(x) = x ** 2에서 x에 따른 y 좌표
    init_x = -2 # 최소값을 찾기 위해 시작할 x 좌표

    for _ in range(5):
        # x = init_x에서의 접선의 기울기 찾기
        gradient = difference_quotient(f, init_x, h=0.01)
        # 접선을 그래프로 그리기 위해
        tangent_estimates = [tangent(x, gradient, init_x, f(init_x)) for x in xs]

        plt.plot(xs, tangent_estimates, label=f'x = {init_x}')

        # x 좌표를 새로운 좌표로 이동
        init_x = move(init_x, gradient, step=-0.1)

    plt.plot(xs, ys, color='black')
    plt.legend()
    plt.ylim(bottom=-1)
    plt.show()

    # 임의의 점에서 시작해, y - x ** 2의 최소값을 찾음
    random.seed(1128)
    init_x = random.randint(-10, 10)
    print(init_x)  # 시작 x 값 = -8
    tolerance = 0.0000001 # 두 x 좌표 사이의 거리가 tolerance 이하면, 반복문 종료
    count = 0
    while True:
        count += 1
        # x 좌표에서 접선의 기울기 계산
        gradient = difference_quotient(f, init_x, h=0.001)
        # 찾은 접선의 기울기를 이용해서 x 좌표를 이동
        next_x = move(init_x, gradient, step=-0.9)
        print(f'{count} : x = {next_x}')

        if abs(next_x - init_x) < tolerance:
            # 이동 전, 후의 x값의 차이가 tolerance 미만이면 반복문 종료
            break
        else:
            # 이동한 점은 다음 반복 때는 시작 점이 됨.
            init_x = next_x

    # 1 : x = 6.399100000007081
    # 2 : x = -5.120180000008816
    # 3 : x = 4.095244000010297
    # ...
    # 84 : x = -0.000500057892426116
    # 85 : x = -0.0004999536860591072
    # 86 : x = -0.0005000370511527142
