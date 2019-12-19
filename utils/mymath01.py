"""
mymath01.py
"""
pi = 3.14

def add(x: int, y: int) -> int:
    """
    두 정수가 주어졌을때, x + y를 리턴

    :param x: 정수 1
    :param y: 정수 2
    :return: x + y
    """
    return x + y

def sub(x: int, y: int) -> int:
    """
    두 정수가 주어졌을때, x - y를 리턴

    :param x: 정수 1
    :param y: 정수 2
    :return: x - y
    """
    return x - y

if __name__ == '__main__':
    print(__name__)
    print('pi = ', pi)
    print('add = ', add(1, 2))
    print('sub = ', sub(1, 2))
# 이 모듈(파일)에서는 main문으로서 위의 코드들이 실행되지만,
# 다른 모듈(파일)에서 import를 해 사용할 경우, 실행 되지 않는다.(main문이 아니기 때문)


