"""

"""
# 함수 정의
def test(x, y):
    print(f'x = {x}, y = {y}')
    return x + y, x - y

# 함수 호출
# test()
# TypeError: test() missing 2 required positional arguments: 'x' and 'y'
# 파이썬은 함수의 parameter의 타입은 검사를 안하지만, 개수는 검사를 한다.

# positional argument ~> 함수를 호출할 때 전달하는 값(argument)이 함수 정의에 따른 순서대로 전달되는 방식
plus, minus = test(1, 2) # x = 1, y = 2
plus, minus = test(2, 1) # x = 2, y = 1

# keyword argument ~> 함수를 호출 할 때 argument를 'parameter = 값'형식으로 전달하는 방식
# keyword argument를 사용하면 함수에 정의된 파라미터 순서와 상관 없이 argument를 전달 가능하다.
plus, minus = test(x=10, y=20) # x = 10, y = 20
print(minus) # -10
plus, minus = test(y=10, x=20) # x = 20, y = 10
print(minus) # 10

# default argument ~> 함수를 정의할 때 paprameter의 기본값을 설정하는 것
def show_msg(msg : str, times : int = 1) -> None: # times의 default를 1로 설정하
    print(msg * times)

show_msg('졸려죽겠다.', 5) # 호출하면서 'times'를 5로 설정함
show_msg('집에가고싶다.') # 'times'의 default가 1이기 때문

# default argument를 갖는 파라미터는
# 반드시 default argument를 갖지 않는 파라미터들이 선언된 뒤에 선언해야 함
# def test2(x = 1, y):
#     return x + y








