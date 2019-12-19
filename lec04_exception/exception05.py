"""
try: except 구문을 함수에 응용하기.
"""
def user_input():
    """
    사용자에게 1, 2, 3 중 하나의 숫자를 입력하도록 함.
    그리고 사용자가 입력한 숫자를 리턴함.
    1, 2, 3 이외의 숫자 또는 문자를 입력하면 크게 혼내고 다시 입력 받기.

    :return: 사용자가 입력한 숫자.(반드시 1, 2, 3 중 하나)
    """
    while True:
        try:
            try:
                x = int(input('[1] 가위 [2] 바위 [3] 보 선택해라 >>>'))
            except ValueError:
                raise ValueError('문자 ㄴㄴ 숫자만 입력해')
            if x in (1, 2, 3):
                return x
            else:
                raise ValueError('정신차려. 1, 2, 3 중에 하나만 고르라고 했어.')
        except ValueError as e:
            print(e.args)

user = user_input()
print('input : ', user)