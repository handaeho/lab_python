"""
가위 바위 보 게임 만들기
1번 : 가위 / 2번 : 바위 / 3번 : 보
사용자 선택 후, 컴퓨터와 가위 바위 보. 승자 출력까지
"""
import numpy as np

print('가위 바위 보 게임!')
print('=============================')
print('[1] 가위', '[2] 바위', '[3] 보')
print('=============================')

user = int(input('[1], [2], [3] 선택하세요 >>>'))
computer = np.random.randint(1, 4) # 1 ~ 4 사이 정수값 난수 생성

if (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
    print('Congret! User Win!')
elif user == computer:
    print('Draw!')
else:
    print('User Lose...')
print(f'user : {user}, computer:{computer}')
