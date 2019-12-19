"""
while 반복문:
[초기 식]
while 조건식:
    True인 동안 실행할 문장
    [변경 식]
    [break]
"""
#1, 2, 3, ..., 10
n = 1
while n <= 10:
    print(n, end=' ')
    n += 1
print()

# 구구단 2단
n = 1
while n < 10:
    print(f'2 x {n} = {2 * n}')
    n += 1

# 구구단 2단 ~ 9단
print('----------')
dan = 2
while dan < 10:
    n = 1
    while n < 10:
        print(f'{dan} x {n} = {dan * n}')
        n += 1
    dan += 1
    print('----------')




