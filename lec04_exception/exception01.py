"""
error, exception : 프로그램 실행 중, 발생할 수 있는 오류

프로그램 실행 중, 오류가 발생했을 때, 해결 방법
=> 오류가 발생한 위치를 찾아, 발생 하지 않도록 수정 필요.
아니면, 발생 하더라도 무시하고 실행 되도록 프로그램을 작성해야함.
"""
# prnit(1) ~~~> NameError

# int() : 문자열을 정수로 변환 / float() : 문자열을 실수로 변환
n = int(input('input >>>')) # 입력된 내용이 문자열이 아닌 정수로 n에 저장
n1 = int('123') # '123'이 문자열이 아닌 정수로 n1에 저장
# n1 = int('123.') ~~~> '.' 때문에 ValueError 발생(정수로 바꿀 수 없기 때문)

numbers = [1, 2, 3]
# print(numbers[3]) ~~~> 범위 내에 없는 index를 출력하려고 하니까 IndexError 발생

# print('123' + 456) ~~~> 문자열('123')과 숫자(456)은 타입이 달라 '+'를 할 수 없음. TypeError 발생

# print(123/ 0) ~~~> ZeroDivisionError: division by zero. 0으로 나누기 불가


