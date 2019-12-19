# for - in

while True:
    print('[1] 전체 구구단 [2] x단 구구단 [3] x단 x개 구구단 [4] 종료')
    print('============================================')
    a = int(input('기능 선택 >> '))

    # 2단 ~ 9단 구구단 출력
    if a == 1:
        for i in range(2, 10):
            for j in range (1, 10):
                print(i, ' * ' , j, '=', i*j)
    # 사용자 입력 받아 구구단 출력
    if a == 2:
        x = int(input('몇 단? >>> '))
        for x in range(x, x+1):
            for i in range (2, 10):
                print(x, ' * ' , i, '=', x*i)
    # x단 x개 구구단
    if a == 3:
        for i in range(2, 10):
            for j in range(1, i+1):
                print(i, ' * ' , j, '=', i*j)
    # 종료
    if a == 4:
        break

# =====================================================================
