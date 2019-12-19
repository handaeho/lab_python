"""
<<<확률>>>

1) 사건 공간(Universe Of Events) - 사건들의 전체 집합
2) 사건(Event) - 각 변수의 상태(ex)동전 앞, 뒷면)
3) 확률(Probability) - 발생할 가능성
"""
import random
from collections import Counter
# ----------------------------------------------------------------------------------------------

# 동전 1개를 10,000번 던지는 실험 ~~~> 앞면 확률 vs 뒷면 확률이 50%에 수렴함을 증명

coin = ['H', 'T']
dice = [1, 2, 3, 4, 5, 6]
print(random.choice(coin))
print(random.choice(dice))

H_state = 0
T_state = 0
for i in range(10000):
    state = random.choice(coin)
    if state == 'H':
        H_state += 1
    else:
        T_state += 1
print(f'H = {H_state} / T = {T_state}')
print('H % = ', H_state / 100)
print('T % = ', T_state / 100)

# ----------------------------------------------------------------------------------------------

# 동전 2개를 10,000번 던지는 실험
# 1) 앞면의 개수가 1개일 경우 ~~~> HT, TH
# 2) 첫 번째 동전이 앞면일 경우 ~~~> HH, HT
# 3) 적어도 한 개의 동전이 앞면일 경우 ~~~> HH, HT, TH

coin1 = ['H', 'T']
coin2 = ['H', 'T']
trials = 10000 # 횟수
x = 0
y = 0
z = 0

# 1)
print('앞면의 개수가 1개일 확률은 약 50%?')
for i in range(trials):
    coin1_state = random.choice(coin1)
    coin2_state = random.choice(coin2)

    if coin1_state == 'H' and coin2_state == 'T':
       x += 1
    elif coin1_state == 'T' and coin2_state == 'H':
       x += 1
    else:
       pass
print('횟수 = ', x, '확률 = ', x / trials)

# 2)
print('첫 번째 동전이 앞면일 확률은 약 50%?')
for _ in range(trials):
    coin1_state = random.choice(coin1)
    coin2_state = random.choice(coin2)

    if coin1_state == 'H' and coin2_state == 'H':
       y += 1
    elif coin1_state == 'H' and coin2_state == 'T':
       y += 1
    else:
       pass
print('횟수 = ', y, '확률 = ', y / trials)

# 3)
print('적어도 한 개의 동전이 앞면일 확률은 약 75%?')
for _ in range(trials):
    coin1_state = random.choice(coin1)
    coin2_state = random.choice(coin2)

    if coin1_state == 'H' and coin2_state == 'H':
       z += 1
    elif coin1_state == 'H' and coin2_state == 'T':
       z += 1
    elif coin1_state == 'T' and coin2_state == 'H':
       z += 1
    else:
       pass
print('횟수 = ', z, '확률 = ', z / trials)

# ----------------------------------------------------------------------------------------------

# 동전 3개를 10,000번 던지는 실험
# 앞면의 개수가 1개일 경우 ~~~> HTT, THT, TTH

coin1 = ['H', 'T']
coin2 = ['H', 'T']
coin3 = ['H', 'T']
trials = 10000 # 횟수
k = 0

print('적어도 한 개의 동전이 앞면일 확률은 약 37.5%?')
for _ in range(trials):
    coin1_state = random.choice(coin1)
    coin2_state = random.choice(coin2)
    coin3_state = random.choice(coin3)

    if coin1_state == 'H' and coin2_state == 'T' and coin3_state == 'T':
       k += 1
    elif coin1_state == 'T' and coin2_state == 'H' and coin3_state == 'T':
       k += 1
    elif coin1_state == 'T' and coin2_state == 'T' and coin3_state == 'H':
       k += 1
    else:
       pass
print('횟수 = ', k, '확률 = ', k / trials)

# ----------------------------------------------------------------------------------------------

# 함수를 사용한 Ver.

def experiment(type, n, t):
    """
    :param type: 실험 타입(동전 던지기, 주사위 던지기 등등)
    :param n: 동전이나 주사위의 개수
    :param t: 동전을 던지는 횟수
    :return: 리스트
    """
    cases = [] # 동전을 던지는 모든 실험 결과를 저장하는 리스트
    for _ in range(t): # 횟수만큼 반복
        case = [] # 각 실험의 결과를 저장할 리스트
        for _ in range(n): # 동전이나 주사위 개수 만큼 반복
            rand = random.choice(type)
            case.append(rand) # 1회 실험 결과를 저장
        cases.append(tuple(case)) # 1회 실험이 끝날 때마다 모든 실험 결과를 저장하는 리스트에 튜플로 저장
        # Hash 알고리즘 ~~~> 정렬을 위한 알고리즘
        # 리스트는 원소가 변할수 있어서, Hash 알고리즘 사용 X. 즉, 고정된 순서를 갖도록 정렬 불가.
        # 따라서 리스트를 정렬하려면 원소가 변하지 않는 '튜플(tuple)'로 변환해야 한다.
        # 즉, Counter 클래스는 tuple의 개수는 셀 수 있지만, list의 개수는 셀 수 없다.
        # 그래서 리스트(list)를 튜플(tuple)로 변환하는 것.
    return cases

print('********************************************************')

# 동전 2개를 던지는 경우
coin_exp = experiment(coin, 2, 10000)
print(coin_exp) # [['T', 'T'], ['T', 'T'], ['T', 'T'], ['T', 'H'], ['H', 'T'], ['T', 'T'], ['H', 'H'], ...
print(len(coin_exp)) # 10000

coin_event_count = Counter(coin_exp)
print(coin_event_count) # Counter({('H', 'T'): 2594, ('T', 'H'): 2534, ('H', 'H'): 2470, ('T', 'T'): 2402})

def how_many_heads(x): # 동전의 앞면이 몇번 나왔는가? ~~~> 모든 'H'의 개수를 센다.
    counter = Counter(x)
    print(counter)
    return counter['H']

print('********************************************************')

# 1) 앞면의 개수가 1개일 경우 ~~~> HT, TH
num_of_cases = 0
for ev, cnt in coin_event_count.items():
    if how_many_heads(ev) == 1:
        num_of_cases += cnt
p_h1 = num_of_cases / trials
print('앞면이 1개일 확룰', p_h1)

print('********************************************************')

# 2) 첫 번째 동전이 앞면일 경우 ~~~> HH, HT
num_of_cases = 0
for ev, cnt in coin_event_count.items():
    if ev[0] == 'H': # 0번지 인덱스의 값이 'H'일때
        # 같은 의미 ~~~> ev == ('H', 'H') or ev == ('H', 'T')
        num_of_cases += cnt # 카운트 증가
p_first_h = num_of_cases / trials
print('첫 번째 동전이 앞면인 확률 = ', p_first_h)

print('********************************************************')
# 3) 적어도 한 개의 동전이 앞면일 경우 ~~~> HH, HT, TH
num_of_cases = 0
for ev, cnt in coin_event_count.items():
    if how_many_heads(ev) == 1 or how_many_heads(ev) == 2:
        num_of_cases += cnt # 카운트 증가
p = num_of_cases / trials
print('적어도 한 개의 동전이 앞면인 확률 = ', p)

print('####################')

# '여사건'을 이용해서 풀 수도 있다.
# 1 - 모두 뒷면이 나올 확률 = 적어도 한 개는 앞면이 나올 확률
num_of_cases = 0
for ev, cnt in coin_event_count.items():
    if how_many_heads(ev) == 0: # 모두 뒷면이 나오는 횟수를 구해서
        num_of_cases += cnt
p_1 = num_of_cases / trials # 모두 뒷면이 나올 확률
print('적어도 한 개의 동전이 앞면인 확률 = ', 1 - p_1)
# 1 - 모두 뒷면이 나올 확률 = 적어도 한 개는 앞면이 나올 확률

print('********************************************************')

# H = 1, T = 0으로 생각하면 ~> coin = [1, 0]
coin2 = [1, 0]
cases = []
for _ in range(trials):
    num_of_heads = 0
    for _ in range(2):
        num_of_heads += random.choice(coin2)
        # coin2를 던져서 나온 결과를 num_of_heads에 증가
    cases.append(num_of_heads)
print(cases[0:10]) # [2, 1, 1, 1, 1, 1, 2, 1, 1, 0]

coin_event_counts = Counter(cases)
print('p(H = 0) = ', coin_event_counts[0]) # H = 0인 횟수가 몇번? (앞면이 안 나올)
print('p(H = 0) = ', coin_event_counts[0] / trials) # H = 0인 확률이 얼마?
print('p(H = 1) = ', coin_event_counts[1]) # H = 1인 횟수가 몇번? (앞면이 한 번 나올)
print('p(H = 1) = ', coin_event_counts[1] / trials) # H = 1인 확률이 얼마?
print('p(H = 2) = ', coin_event_counts[2]) # H = 2인 횟수가 몇번? (앞면이 두 번 나올)
print('p(H = 2) = ', coin_event_counts[2] / trials) # H = 2인 확률이 얼마?

print('********************************************************')

# 동전 3개를 10,000번 던지는 실험
# 앞면의 개수가 1개일 경우 ~~~> HTT, THT, TTH

# 동전 3개를 던지는 경우
coin_exp = experiment(coin, 3, 10000)
print(coin_exp[0:10]) # [('T', 'H', 'T'), ('T', 'T', 'T'), ('H', 'T', 'T'), ('H', 'T', 'T'), ...
print(len(coin_exp)) # 10000

coin_event_count = Counter(coin_exp)
print(coin_event_count) # Counter({('T', 'H', 'H'): 1314, ('H', 'H', 'T'): 1281, ('T', 'H', 'T'): 1278, ...

def how_many_heads_3(x): # 동전의 앞면이 몇번 나왔는가?
    counter = Counter(x)
    print(counter)
    return counter['H']

print('********************************************************')

# 주사위 2개를 던지는 경우
dice_exp = experiment(dice, 2, 10000)
print(dice_exp[0:10]) # [(2, 5), (4, 5), (2, 4), (2, 3), (1, 5), (5, 4), (3, 6), (1, 6), (2, 2), (4, 1)]
print(len(dice_exp)) # 10000

dice_event_count = Counter(dice_exp)
print(dice_event_count) # Counter({(6, 3): 315, (3, 2): 308, (4, 6): 307, (4, 5): 304, (6, 1): 303, ...

# 주사위 2개를 던져 두 눈의 합이 8이 나오는 확률
# (2, 6), (3, 5), (4, 4), (5, 3), (6, 2) ~~~> 5/36
num_of_8 = 0
for ev, cnt in dice_event_count.items():
    dice_8 = ev[0] + ev[1] # 두 주사위 눈을 더함
    if dice_8 == 8: # 두 눈의 합이 8이면
        num_of_8 += cnt # 그 눈의 조합이 나온 횟수를 더한다.
print(f'두 주사위의 합이 8인 확률 = {num_of_8 / trials}%')

print('********************************************************')

# 주사위 2개를 던져 적어도 둘 중 하나가 짝수가 나올 확률
# (1, 1), (1, 3), (1, 5), (3, 1), (3, 3), (3, 5), (5, 1), (5, 3), (5, 5)를 제외한 모든 경우 ~~~> 27/36
num_of_even = 0
for ev, cnt in dice_event_count.items():
    if ev[0] % 2 == 1 and ev[1] % 2 == 1: # 두 주사위가 모두 홀수인 경우를 구해
        num_of_even += cnt
print(f'두 주사위가 적어도 둘 중 하나는 짝수일 확률 = {1 - (num_of_even / trials)}%') # 여사건으로 구함














