"""
Variable-length keyword Argument(가변 길이 키워드 인수)
: 함수 정의시, parameter 앞에 '**'를 사용.
함수 내부에서는 dict 취급됨.
"""
def test(**kargs):
    print(kargs)
    for key in kargs:
        print(key, kargs[key]) # name daeho age 26

test() # {}
test(name='daeho', age=26) # {'name': 'daeho', 'age': 26}
# 파라미터로 키워드와 해당 값을 전달하면, 함수 내부에서 key:value형태로 전달받아 dict 형태로 리턴한다.


