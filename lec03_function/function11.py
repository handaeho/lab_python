"""
lambda 표현식(lambda expression) : 함수의 이름 없이, 매개변수 선언 & 리턴 값으로만 표현하는 방법.

1) f(x) = ax + b
2) f:x -> ax + b ~~~~~> lambda(람다) 표기법
=> 1, 2 두개는 같은 의미의 함수. 표기법만 다른 것.

- 표현 방법 : lambda [parameter1, parameter2, ...]: 식(expression)

'lambda 표현식'은 '이름이 없는 함수' . 따라서 호출하려면, 어떤 변수에 저장 해주어야함.
그래서 lambda 표현식은 '함수의 매개변수로 함수를 전달'하고자 할 때 주로 사용.
"""
# lambda 표현식 사용
mltiplication = lambda x, y: x * y
result_mlt = mltiplication(2, 4)
print(result_mlt)

division = lambda x, y: x / y
result_div = division(8, 2)
print(result_div)

# -------------------------------------------------------------------

# 함수의 매개변수로 함수 전달시, lambda의 사용
def calc(x, y, op):
    return op(x, y)

result_calc = calc(1, 2, lambda x, y: x + y) # lambda 표현식이 매개변수 'op'로 전달됨.
print(result_calc)
# x + y 연산을 하는 함수를 만들고, calc() 함수 안에서 호출 한 것과 같은 결과.

# -------------------------------------------------------------------
# lambda 표현식을 사용한 함수 예제
def my_filter(values, func):
    """
    어떤 리스트를 받아 필터링 조건을 만족하는 원소들만으로 이루어진
    새로운 리스트를 생성하고 리턴하는 함수.

    :param values: 리스트
    :param func: True / False를 리턴하는 함수
    :return: 필터링 조건에 만족하는 원소들로 이루어진 새로운 리스트
    """
    result = [] # 빈 리스트 생성
    for item in values: # parameter에 전달된 리스트에서 원소를 하나씩 꺼냄
        if func(item): # 필터링 조건 함수인 func()의 리턴 값을 검사해, True의 경우에만
            result.append(item) # result 리스트에 추가
    return result # 필터링 된 result 리스트 리턴

numbers = [1, 2, 3, 4, 5, 6]

filtered_result = my_filter(numbers, lambda x: x > 3)
print(filtered_result) # [4, 5, 6]
# 리스트를 my_filter() 함수로 전달하는데,
# x(전달된 리스트)가 3보다 크면(= 필터링 조건식), result 리스트에 추가.
# 즉, lambda 표현식인 'x: x > 3'이 'func'가 되는 것이다.

even = my_filter(numbers, lambda x: x % 2 == 0)
print(even) # [2, 4, 6]

languages = ['python', 'r', 'pl/sql', 'java', 'c/c++']
more_than_5 =my_filter(languages, lambda x: len(x) > 5)
print(more_than_5)

def my_filter2(values, func):
    return [x for x in values if func(x)] # func(x)를 만족하는 values내의 x들의 리스트
# 즉, 더 짧지만 my_filter과 같은 기능을 한다.

print(my_filter2(numbers, lambda x: x > 3)) # [4, 5, 6]

def my_mapper(values, func):
    """
    리스트의 아이템들을 함수의 파라미터에 전달해,
    리스트 아이템을 key, 함수의 리턴 값을 values로 하는 dict를 리턴

    :param values: 리스트
    :param func: 파라미터가 1개인 함수
    :return: dict
    """
    result = {} # 빈 dict 생성
    for item in values: # 리스트 values의 모든 원소들을 반복
        # dict의 key는 item, dict의 values는 func()함수의 리턴 값
        result[item] = func(item)
    return  result

mapper_result = my_mapper(languages, lambda x: len(x))
# languages 리스트의 원소를 key로, 각 원소의 길이를 values로 하는 dict 생성
print(mapper_result)
# item = 각 원소 / values = func(). 즉, len()의 리턴 값인 각 원소의 길이
# {'python': 6, 'r': 1, 'pl/sql': 6, 'java': 4, 'c/c++': 5}

def my_mapper2(values, func):
    return {key : func(key) for key in values}
    # key는 values의 각 원소, values는 func()의 각 리턴값이므로

mapper_result2 = my_mapper2(languages, lambda x: len(x))
print(mapper_result2) # {'python': 6, 'r': 1, 'pl/sql': 6, 'java': 4, 'c/c++': 5}
# my_mapper보다 짧지만 같은 기능.

