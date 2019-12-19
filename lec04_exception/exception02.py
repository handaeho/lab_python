"""
오류가 발생하면 무시하고 실행 되게 하려면? => try: ~ except 구문

try:
    정상적으로 실행 될 문장
except 에러종류: [as 별명]
    에러 발생시, 실행 될 문장등
[except 다른에러: 코드]
[else:]
    [에러 없이 try 블록 안의 모든 문장이 정상 실행 되었을 때 실행될 문장들]
[finally:]
    [에러 발생 여부와 관계없이 반드시 실행될 문장들]
"""
try:
    numbers = [1, 2, 3]
    for index, values in enumerate(numbers):
        print(index, ':', values, end=' ')
    print()
except IndexError:
    print('IndexError Occured')
else:
    print('try 블록의 모든 내용을 정상 실행 ')
finally:
    print('finally 블록')
# 0 : 1  1 : 2  2 : 3
# try 블록의 모든 내용을 정상 실행
# finally 블록 ~~~> 에러 없으므로 try 블록이 정상 실행 후 else, finally 블록을 출력하며 종료

# ----------------------------------------------------------------------------

try:
    numbers = [1, 2, 3]
    for i in range(1, 4):
        print(index, ':', numbers[i], end=' ')
    print()
except IndexError:
    print('IndexError Occured')

else:
    print('try 블록의 모든 내용을 정상 실행 ')
finally:
    print('finally 블록')
# 2 : 2 2 : 3 IndexError Occured
# finally 블록 ~~~> 에러가 발생했으므로 except 블록이 실행되고 finally 블록을 출력하며 종료
# else 블록은 '에러 없이 정상 실행'되었을때만 실행

# ----------------------------------------------------------------------------

try:
    numbers = [1, 2, 3]
    for i in range(1, 4):
        print(index, ':', numbers[i], end=' ')
    print()
except ValueError: # IndexError인데 ValueError로 하면
    print('IndexError Occured')

else:
    print('try 블록의 모든 내용을 정상 실행 ')
finally:
    print('finally 블록')
# IndexError: list index out of range ~~~> except 블록이 실행 되지 못하고 finally 블록만 출력
# 왜? except에 선언한 에러와 발생한 에러가 다르기 때문.

# ----------------------------------------------------------------------------

try:
    numbers = [1, 2, 3]
    for i in range(1, 4):
        print(index, ':', numbers[i], end=' ')
    print()
except ValueError:
    print('ValueError Occured')
except IndexError:
    print('IndexError Occured') # except 블록을 두개 선언
else:
    print('try 블록의 모든 내용을 정상 실행 ')
finally:
    print('finally 블록')
# 2 : 2 2 : 3 IndexError Occured
# finally 블록
# ValueError와 IndexError 두개를 선언하였고, IndexError가 발생 해서, 그에 해당하는 except 블록이 실행됨.


