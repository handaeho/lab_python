"""
<<<확률 변수(Random Variable)>>> : 어떤 확률 분포와 연관 되어 있는 변수.

1) 동전 1개를 던지는 확률 분포에서 동전 앞면의 개수 X
P(X=1) = 1/2, P(X=0) = 1/2
2) 동전 1개를 던지는 확률 분포에서 동전 뒷면의 개수 Y
P(Y=1) = 1/2, P(Y=0) = 1/2
3) 주사위 1개를 던지는 확률 분포에서 주사위 눈의 개수 Z
P(Z=1, 2, 3, 4, 5, 6) = 각 1/6

기대값 : 확률 변수의 확률에 확률 변수의 값을 가중 평균 한 값
E(X) = sum(X_i * P(X_i))

동전 1개를 던질때, 동전 앞면의 기대값
E = (1 * 1/2) + (0 * 1/2) = 1/2 = 0.5 ((앞면 * 앞면 확률) + (뒷면 * 뒷면 확률))
주사위 1개를 던질때, 주사위 눈의 기대값
E = (1 * 1/6) + (2 * 1/6) + ... + (6 * 1/6) = 3.5 ((눈 1 * 1일 확률) + ... + (눈 6 * 6일 확률))
"""
# 동전 3개를 던질때, 확률 변수 = 동전의 앞면
# X = 0, 1, 2, 3
# 동전 3개를 10,000번 던지는 실험
# -> P(X=0) = 1/8, P(X=1) = 3/8, P(X=2) = 3/8, P(X=3) = 1/8
# 기대값 : ((0 * 1) + (1 * 3) + (2 * 3) + (3 * 1)) / 8 = 1.5
import random
from collections import Counter

experiments = [] # 동전 3개를 10,000번 던질때, 동전 앞면 개수 리스트
coin = (1, 0) # 1 = 앞 / 0 = 뒤
trials = 10000
for _ in range(trials):
    head = 0 # 동전 앞면 개수
    for _ in range(3):
        head += random.choice(coin)
    experiments.append(head)
print(experiments[0:10]) # [3, 2, 0, 1, 2, 1, 1, 3, 2, 1, ...]  ~~~> 앞면이 3번, 2번 0번, ... 나왔다.

head_counts = Counter(experiments) # 각 원소의 개수 집계
print(head_counts) # Counter({2: 3786, 1: 3717, 3: 1300, 0: 1197}) ~~~> key: value 형태

expected_value = 0
for x, cnt in head_counts.items(): # head_counts.items() ~~~> 각 원소의 개수. 즉, value.
    expected_value += x * (cnt / trials) # (cnt / trials) = (횟수 / 전체) ~~~> 확률
    # x * (cnt / trials) = (0 * 1197/10000) + (1 * 3717/10000) + (2 * 3786/10000) + (3 * 1300/10000)
print('동전 3개를 던져 앞면의 기대값은 = ', expected_value) # 동전 3개를 던져 앞면의 기대값은 =  1.5071

# 주사위 눈의 기대값 ------------------------------------------------------------------------------------
dice = (1, 2, 3, 4, 5, 6)
experiments = [random.choice(dice) for _ in range(trials)] # 10000번 주사위 던져 나온 눈을 experiments 리스트에 저장
print(experiments[0:10]) # [4, 2, 6, 6, 6, 1, 1, 4, 5, 2, ...]

head_counts = Counter(experiments)
print(head_counts) # Counter({5: 1723, 3: 1713, 1: 1689, 4: 1645, 6: 1619, 2: 1611})

expected_value = 0
for x, cnt in head_counts.items():
    expected_value += x * (cnt / trials)
print('주사위 1개를 던져 주사위 눈의 기대값은 = ', expected_value) # 주사위 1개를 던져 주사위 눈의 기대값은 =  3.5198







