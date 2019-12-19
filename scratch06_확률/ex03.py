"""
<<<조건부 확률>>>

P(A) : 사건 A가 발생할 확률
P(B) : 사건 B가 발생할 확률
P(A, B) : 사건 A와 사건 B가 동시에 발생할 학률(A, B의 교집합 확률)
P(A|B) : 사건 B가 발생시, 사건 A가 발생할 확률 ~~~> '조건부 확률'

P(A|B) = P(A, B) / P(B)
만약, A와 B가 독립 사건이면, P(A ,B) = P(A)P(B)이므로,  P(A|B) = P(A, B) / P(B) =  P(A)P(B) / P(B) = P(A)이다.

자녀가 2명 있는 가정에서
A :  첫째가 딸인 경우. P(A) = 1/2
B :  두 자녀가 모두 딸인 경우. P(B) = 1/4
C : 두 자녀 중, 최소 한 명이 딸인 경우. P(C) = 3/4

P(A, B) = P(A)P(B) = 1/4 = P(B, A)
P(A, C) = P(A)P(C) = 1/2 = P(C, A)
P(B, C) = P(B)P(C) = 1/4 = P(C, B)

P(B|A) = P(첫째가 딸일때, 두 자녀 모두 딸일 확률) = P(B, A) / P(A) = 0.25 / 0.5 = 0.5
P(C|A) = P(첫째가 딸일때, 최소 한명은 딸일 확률) = P(C, A) / P(A) = 0.5 / 0.5 = 1
P(B|C) = P(적어도 한 명이 딸일때, 두 자녀 모두 딸인 경우) = P(B, C) / P(C) = 0.25 / 0.75 = 약 0.3
"""
import random

kid = ('boy', 'girl')
trials = 10000
older_girl = 0 # 첫째가 딸
both_girl = 0 # 둘 다 딸
either_girl = 0 # 둘 중 한 명이 딸

for _ in range(trials):
    older = random.choice(kid)
    younger = random.choice(kid)

    if older == 'girl':
        older_girl += 1
    if older == 'girl' and younger == 'girl':
        both_girl += 1
    if older == 'girl' or younger == 'girl':
        either_girl += 1

# 첫째가 딸이면 두 자녀 모두 딸일 확률
p1 = both_girl / older_girl # P(B, A) / P(A)
print('P(첫째가 딸일때, 둘 다 딸인 확률) = ', p1)
# P(첫째가 딸일때, 둘 다 딸인 확률) =  0.5020136931131696

# 적어도 한명이 딸일떄, 둘 다 딸일 확률
p2 = both_girl / either_girl # P(B, C) / P(C)
print('P(적어도 한명이 딸일떄, 둘 다 딸일 확률) = ', p2)
# P(적어도 한명이 딸일떄, 둘 다 딸일 확률) =  0.33369026904028914

