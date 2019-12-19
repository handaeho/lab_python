"""
함수 정의
def 함수이름(파라미터1 : 타입, 파라미터2 : 타입, ...) -> 리턴 타입:
    함수의 기능(body)
"""
def sub(x : int, y : int) -> int:
    return x - y

result = sub(1, 2)
print(result)
# 파이썬은 함수를 호출할 때, 함수 파라미터 타입과 리턴 타입을 검사하지는 않는다.
result2 = sub(1.1, 0.9)
print(result2) # 0.20000000000000007 그래서 이렇게 int로 힌트를 주었지만 float를 넣어도, 에러는 없다.

def my_sum(numbers : list) -> float:
    """
    숫자(int나 float 등)들이 저장된 리스트를 받아, 모든 원소의 합을 리턴하는 함수
    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트내의 모든 원소의 합
    """
    sum_n = 0
    for i in numbers:
    # numbers 리스트는 위에서 만들었다고 보고, 별도의 선언 없이 그냥 사용해도 된다.
        sum_n = sum_n + i
    return sum_n
    # return [sum(numbers)] ~~~> 이렇게 sum()함수를 사용해도 된다.

mysum = my_sum([1, 2, 3, 4, 5])
print(mysum) # [15]

def my_avg(numbers : list) -> float:
    """
    숫자 리스트를 받아, 평균을 구해 리턴하는 함수
    :param numbers: 숫자들의 리스트
    :return: 리스트내의 모든 원소들의 평균
    """
    # import numpy as np
    sum_n = 0
    for i in numbers:
       sum_n = sum_n + i
    avg_n = sum_n / len(numbers)
    return avg_n
    # return [np.mean(numbers)] ~~~> 이렇게 np.mean() 함수를 사용해도 된다.
result_avg = my_avg([1, 2, 3, 4, 5])
print(result_avg)

