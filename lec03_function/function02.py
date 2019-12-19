"""
Function define / declaration

def 함수 이름(파라미터 선언, ...):
    함수 기능 작성
    [return 값]
"""
def say_hello():
    """
    # 함수를 설명하는 주석
    'Hello'를 출력하는 함수
    :return: None
    """
    print('Hello')
# 함수는 '호출'해야지만 실행됨.
say_hello()

def print_msg(msg):
    """
    인수 msg를 출력하는 함수
    :param msg: world
    :return:
    """
    print(msg)

print_msg('World') # 'World'를 parameter로 전달하고 받아, 해당 Argument(msg) 출력.

def add(x, y):
    """
    숫자 2개를 전달 받아 더하는 함수
    :param x: 더할 숫자 1
    :param y: 더할 숫자 2
    :return: x + y
    """
    return x + y

result = add(3, 7)
print(result)

def sum_and_product(x, y):
    """
    숫자 2개를 전달 받아 합과 곱을 수행하는 함수
    :param x: 숫자 1
    :param y: 숫자 2
    :return: x + y, x * y
    """
    return x + y, x * y

result_sp = sum_and_product(3, 7)
print(result_sp) # (10, 21) ~~~> tuple 형태로 출력됨

def person(name, age):
    """
    이름과 나이를 전달받아 dict를 만들어 출력하는 함수
    :param name: 이름
    :param age: 나이
    :return: {'name' : name, 'age' :age}
    """
    return {'name' : name, 'age' : age}

person_v = person('daeho', 26)
print(person_v) # {'name': 'daeho', 'age': 26}

