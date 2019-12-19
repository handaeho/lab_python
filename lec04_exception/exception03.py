"""
try: ~ except 연습
"""
while True:
    try:
        n = int(input('정수 input >>>'))
        print('n = ', n)
    except ValueError:
        print('정수를 입력 하라구요...')
    else:
        print('잘했어요. 이제 꺼져')
        break
    finally:
        print('------------------------')


