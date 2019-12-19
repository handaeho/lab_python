"""
list comprehension

tuple : (1, 2, 3) / list : [1, 2, 3] / set : {1, 2, 3} / dict : {a:1, b:2, c:3}
"""
import numpy as np

numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers2 = []
for n in range(1, 6):
    numbers2.append(n)
print(numbers2)

numbers3 = [n for n in range(1, 6)]
print(numbers3)

# 2, 4, 6, 8, 10
even = [2 * n for n in range(1, 6)]
print(even)

# 1, 4, 9, 16, 25
squares = [n ** 2 for n in range(1, 6)]
print(squares)

# 난수 10개 배열
randoms = [np.random.randint(0, 101) for _ in range(10)]
print(randoms)

even2 = []
for n in range(1, 11):
    if n % 2 == 0:
        even2.append(n)
print(even2)

even3 = [n for n in range(1, 11) if n % 2 == 0]
print(even3)

# 주사위 두개를 던졌을 때 경우의 수 (1 ~ 6) (1 ~ 6)
dice1 = []
for x in range(1,7):
    for y in range(1, 7):
        dice1.append((x, y)) # (x, y) 튜플을 리스트에 추가
print(dice1)

dice2 = [(x, y) for x in range(1, 7) for y in range(1, 7)]
print(dice2)

dice3 = []
for x in range(1, 7):
    for y in range(1, 7):
        if x >= y:
            dice3.append((x, y))
print(dice3)

dice4 = [(x, y) for x in range(1, 7) for y in range(1, 7) if x >= y]
print(dice4)

# 시험 점수 10개 리스트
scores = [np.random.randint(0, 101) for _ in range(10)]
print(scores)

# 평균보다 높은 점수
mean = np.mean(scores)
above_mean = []
for s in scores:
    if s > mean:
        above_mean.append(s)
print(above_mean)

above_mean2 = [ss for ss in scores if ss > mean]
print(above_mean2)



