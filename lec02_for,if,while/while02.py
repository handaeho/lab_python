"""
while 연습
"""
while True:
    print('[1] 입력')
    print('[2] 수정')
    print('[3] 삭제')
    print('[0] 종료')
    print('----------')
    menu = input('메뉴를 선택하세요. >>>')

    if menu == '0':
        break
    elif menu == '1':
        print('입력')
    elif menu == '2':
        print('수정')
    elif menu == '3':
        print('삭제')
print('종료')

