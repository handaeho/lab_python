"""
Function(함수) : 기능을 수행해서 값을 반환하는 코드 블록
Argument(인수) : 함수를 호출할 때, 전달하는 값
Parameter(매개변수) : argument를 저장하기 위해서 함수를 정의할 때, 사용하는 변수

함수 호출(call, invoke)
"""
print('Hello, World') # print() 함수 ~~~> 하지만 return값은 None.

print('hello', 'world', 123) # 이때, argument는 3개

print('hello', end=',') # end => parameter
print('python') # hello,python ~~~> ','로 구분됨. 줄 바뀜은 없음.

# Python 내장 함수
print(sum([1, 2, 3, 4, 5])) # 15

abs_v = abs(-5)
print(abs_v) # 5

power = pow(2, 4, 3) # 2 ** 4 % 3
print(power) # 1