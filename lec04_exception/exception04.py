"""
사용자 정의 오류를 발생시키는 방법 => raise
"""
while True:
    try:
        age = int(input('나이를 입력해라 >>>'))
        # 그런데 이런 경우 -100을 입력하면 논리적으로 맞지 않는다.
        if age < 0:
            raise ValueError('헛소리 하지 말거라.')
            # 그럴 경우, 사용자 정의 오류를 발생시킨다.
        print(f'네 나이는 {age}살 이구나')
    except ValueError as e:
        print(e.args)
        # 나이가 음수로 입력되면, 사용자 정의 오류인
        # ('헛소리 하지 말거라',)를 출력.
        # 문자가 들어오면 숫자로 변환 할 수 없으므로,
        # ("invalid literal for int() with base 10: 'ㅁ'",)를 출력.
    else:
        print('이제 꺼져')
        break
    finally:
        print('--------------------------')