"""
가변 길이 인수(Variable-length Argument) : 함수 호출 시, 전달하는 argument의 개수가 변함.
"""
print('a')
print('a', 'b', 'c', 'd', sep=':')
# 이처럼 print()에는 다양한 개수의 argument가 적용될 수 있다.

# 가변 길이 함수 정의
def fn_vararg(*varargs): # *parameter = 가변 길이
    print(varargs) # (1, 2, 3)
    print(*varargs) # 1 2 3 ~~~> 이렇게 출력하면 tuple이 '분해'되어 출력됨(like print(1, 2, 3))
    for arg in varargs: # 가변 길이 인수는 tuple 취급되기 때문에 for 구문 사용가능
        print(arg)

fn_vararg(1, 2, 3)


def summation(*args):
    """
    임의의 개수인 숫자를 전달 받아, 그 총합을 계산하는 함수
    :param args: 임의의 개수인 숫자들
    :return: 숫자들의 총합
    """
    sum_a = 0
    for i in args:
        sum_a += i
    print(sum_a)

summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def fn_vararg2(a, *b):
    print(f'a = {a}')
    print(f'b = {b}')

fn_vararg2(1) # a = 1 b = (). 가변길이 인수인 b는 안 줘도 실행이 된다. (0개 역시 가변 길이이므로)


def fn_vararg3(*a, b):
    print(f'a = {a}')
    print(f'b = {b}')

# fn_vararg3(1, 2)
# 이렇게 넣으면 1, 2가 가변 길이인 a로 들어가게 되어, b는 비어 있게 된다. 따라서 오류 발생.
# 그러므로 keyword를 주어야 한다.
fn_vararg3(1, b=2)


def calculator(*values, operator):
    """
    operator가 '+'인 경우, 모든 values의 합계 리턴,
    operator가 '*'인 경우, 모든 values의 곱 리턴하는 함수.
    :param values: 더해지거나 곱해질 숫자들
    :param operator: 연산 기호
    :return: 숫자들의 합계 또는 곱
    """
    sum_a = 0
    mul_a = 1
    if operator == '+':
        for i in values:
            sum_a += i
            print(sum_a)
    elif operator == '*':
        for i in values:
            mul_a *= i
            print(mul_a)

calculator(1,2,3,4,5, operator='+')


