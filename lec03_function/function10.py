"""
파이썬에서 함수는 1급 객체(first-class object)
- 함수를 변수에 저장 가능.
- 매개변수(parameter)에 함수 전달 가능.
- 함수가 다른 함수를 리턴 가능.
- 함수 내부에서 다른 함수 정의 가능.
"""
# 함수를 변수에 저장
def twice(x):
    return 2 * x

a = twice(100) # 함수 호출 후, 리턴값 저장
print(a) # 리턴값 출력

double = twice # 함수 자체를 변수에 저장.
print(double) # <function twice at 0x00000296A2CE10D8>

result = double(11)
print(result) # 22
# twice()와 double()은 같은 기능을 하게됨.

# -------------------------------------------------------------------

# 매개변수(parameter)에 함수 전달
def plus(x, y):
    return x + y

def miuns(x, y):
    return x - y

def calculate(x, y, operator):
    return operator(x, y)

result_p = calculate(1, 2, plus) # 연산될 값(x, y)과 연산할 함수
print(result_p) # 3 ~~~> plus() 함수 수행

result_m = calculate(2, 4, miuns)
print(result_m) # -2 ~~~> minus() 함수 수행

# -------------------------------------------------------------------

# 함수 내부에서 다른 함수 정의 & 함수가 다른 함수를 리턴
def decorate(func):
    print('decorate 함수 내부 : ', func.__name__)
    # decorate 함수 내부에서 wrapper_function 함수 정의
    def wrapper_function(*args):
        print('다음 함수를 실행 : ', func.__name__)
        return func(*args)
        # decorate 함수에서 wrapper_function 함수를 리턴
    return wrapper_function # 값이 아닌, 함수 이름 자체를 리턴

wrapper = decorate(print) # decorate 함수 내부 :  print
# wrapper은 '함수'가 되었음.
# print() 함수를 func.__name__에 전달하고, 내부의 wrapper_function()의 *args에 전달.
wrapper('a', 'b', 'c') # 다음 함수를 실행 :  print / a b c
# wrapper은 wrapper_function()(= print())이 되어 전달 받은 함수(func.__name__)의 기능을 수행.

# -------------------------------------------------------------------



