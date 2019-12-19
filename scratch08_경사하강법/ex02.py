"""
경사 하강법 연습
"""
import random

import matplotlib.pyplot as plt
from scratch08_경사하강법.ex01 import f_derivative, difference_quotient, tangent, move


def g(x):
    """ g(x) = (1/3)x ** 3 - x """
    return x ** 3 / 3 - x

if __name__ == '__main__':
    # ex01에서 작성한 함수들을 이용하자.
    xs = [x / 10 for x in range(-30, 31)]

    # 1) g(x) 그래프 그리기
    ys = [g(x) for x in xs]

    plt.plot(xs, ys)
    plt.axhline(y=0, color='0.3')
    plt.axvline(x=0, color='0.3')
    plt.axvline(x=-1, color='0.75')
    plt.axvline(x=1, color='0.75')
    plt.ylim(bottom=-2, top=2)
    plt.show()

    # 2) 극값을 경사 하강법으로 찾기
    # 지역 최소값 찾기
    init_x = random.randint(0, 2)
    print(init_x)
    tolerance = 0.0000001  # 두 x 좌표 사이의 거리가 tolerance 이하면, 반복문 종료
    count = 0
    while True:
        count += 1
        # x 좌표(init_x)에서 접선의 기울기 계산
        gradient = difference_quotient(g, init_x, h=0.001)
        # 찾은 접선의 기울기를 이용해서 x 좌표(init_x)를 이동
        # 최소값을 찾으므로, 기울기의 반대 방향(step이 '-'. 즉, x가 줄어드는 방향)으로 움직인다.
        next_x = move(init_x, gradient, step=-0.1)
        print(f'{count} : x = {next_x}')

        if abs(next_x - init_x) < tolerance:
            # 이동 전, 후의 x값의 차이가 tolerance 미만이면 반복문 종료
            break
        else:
            # 이동한 점은 다음 반복 때는 시작 점이 됨.
            init_x = next_x
        # 1 : x = 1.6997999666667134
        # 2 : x = 1.5106979606687148
        # 3 : x = 1.3823260247024498
        # ...
        # 62 : x = 0.9995005471450473
        # 63 : x = 0.9995004293826808
        # 64 : x = 0.9995003351727965 ~~~> x는 약 1에서 최소 극값을 갖는다.

