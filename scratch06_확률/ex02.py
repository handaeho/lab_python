"""
사건의 종속성 VS ehr립성

사건 A의 발생 여부가 사건 B의 발생 여부에 대한 정보를 제공한다면
(사건 A의 발생 여부가 사건 B에 영향을 미친다면)
사건 A와 사건 B는 '종속 사건(Dependent Event)'

사건 A의 발생 여부가 사건 B의 발생 여부에 대한 정보를 제공하지 않는다면
(사건 A의 발생 여부가 사건 B에 영향을 미치지 않는다면)
사건 A와 사건 B는 '독립 사건(Independent Event)'

1번, 2번 동전 2개를 던지는 경우,
A : 1번 동전이 앞면
B : 2번 동전이 뒷면 ~~~> 사건 A, B는 서로 영향을 미치지 않는다. = A, B는 독립 사건
C : 두 동전 모두 뒷면 ~~~> 사건 A, C는 서로 영향을 미친다. = A, C는 종속 사건

P(A) : 사건 A가 발생할 확률
P(B) : 사건 B가 일어날 확률
P(A, B) : 사건 A와 사건 B의 교집합이 발생할 확률

P(A, B) = P(A) * P(B)가 성립하면, 두 사건은 독립 사건
"""
# 자녀가 2명인 경우
# A : 첫째가 '딸'
# B : 둘째가 '아들'
# C : 둘 다 '딸'

# A / B는 독립 사건이고, A / C는 종속 사건임을 증명
# P(A), P(B), P(C), P(A, B), P(A, C)를 구해라
# ----------------------------------------------------------------------------------------------
import random
from collections import Counter

sex = ['M', 'F'] # M = 남자, F = 여자
child = []
trials = 10000

def exp(n, t):
    for i in range(t):
        c = []
        for j in range(n):
            make_child = random.choice(sex)
            c.append(make_child)
        child.append(tuple(c))
    return child

sex_exp = exp(2, 10000)
print(sex_exp) # [('F', 'M'), ('M', 'M'), ('M', 'F'), ('F', 'M'), ('F', 'M'), ('F', 'F'), ...
print(len(sex_exp)) # 10000

sex_event_count = Counter(sex_exp)
print(sex_event_count) # Counter({('M', 'M'): 2527, ('M', 'F'): 2521, ('F', 'F'): 2492, ('F', 'M'): 2460})

# ----------------------------------------------------------------------------------------------
# P(A) ~~~> 첫째가 딸
num_of_F = 0
for ev, cnt in sex_event_count.items():
    if ev[0] == 'F': # 0번지 인덱스의 값이 'F'일때 (첫째가 딸일 때)
        num_of_F += cnt # 카운트 증가
p_first_F = num_of_F / trials
print('첫째가 딸인 확률 (P(A)) = ', p_first_F)

# ----------------------------------------------------------------------------------------------
# P(B) ~~~> 둘째가 아들
num_of_M = 0
for ev, cnt in sex_event_count.items():
    if ev[1] == 'M':
        num_of_M += cnt
p_second_M = num_of_M / trials
print('둘째가 아들인 확률 (P(B)) = ', p_second_M)

# ----------------------------------------------------------------------------------------------
# P(C) ~~~> 둘 다 딸
num_of_both_F = 0
for ev, cnt in sex_event_count.items():
    if ev[0] == 'F' and ev[1] == 'F':
        num_of_both_F += cnt
p_both_F = num_of_both_F / trials
print('둘 다 딸인 확률 (P(C)) = ', p_both_F)

# ----------------------------------------------------------------------------------------------
# P(A, B) ~~~> 첫째는 딸, 둘째는 아들
num_of_F_M = 0
for ev, cnt in sex_event_count.items():
    if ev[0] == 'F' and ev[1] == 'M':
        num_of_F_M += cnt
p_F_M = num_of_F_M / trials
print('첫째는 딸 / 둘째는 아들인 확률 (P(A, B)) = ', p_F_M)

# ----------------------------------------------------------------------------------------------
# P(A, C) ~~~> 첫째가 딸이면 둘 다 딸
num_of_F_again_F = 0
for ev, cnt in sex_event_count.items():
    if ev[0] == 'F': # 0번지 인덱스의 값이 'F'일때 (첫째가 딸일 때)
        if ev[1] == 'F': # 1번지 인덱스의 값이 'F'면 (둘째도 딸일 때)
            num_of_F_again_F += cnt # 카운트 증가
        else:
            pass
p_F_again_F = num_of_F_again_F / trials
print('첫째가 딸이면 둘째도 딸인 확률 (P(A, C)) = ', p_F_again_F)

# ----------------------------------------------------------------------------------------------
print(f'P(A, B) = {p_F_M}, P(A) * P(B) = {p_first_F * p_second_M}')
print(f'P(A, C) = {p_F_again_F}, P(A) * P(C) = {p_first_F * p_both_F}')
# P(A, B) = 0.2501, P(A) * P(B) = 0.25121124
# P(A, C) = 0.2575, P(A) * P(C) = 0.13070700000000002
# 즉, A와 B는 '독립적' / A와 C는 '종속적'임을 확인 할 수 있다.
