"""
빈 리스트(scores) 선언.
난수 발생 시켜, 리스트에 저장. (0 ~ 100)
scores 리스트, 평균, 최소, 최대 점수, 분산, 표준편차 출력
"""
import numpy as np
from math import sqrt

scores = []
for i in range(10):
    score = np.random.randint(0, 101)
    scores.append(score)
print('scores = ', scores)

# < 내장 함수 이용>

mean = np.mean(scores)
print('mean = ', mean)

min_score = min(scores)
print('min = ', round(min_score, 3))

max_score = max(scores)
print('max = ', round(max_score, 3))

var_score = np.var(scores)
print('var = ', round(var_score, 3))

std_score = np.std(scores)
print('std = ', round(std_score, 3))

# <직접 구현>
avg = sum(scores) / len(scores)
print('avg = ', round(avg, 3))

sum_0f_squares = 0
for score in scores:
    sum_0f_squares += (score - avg) ** 2
std_s = sqrt(sum_0f_squares / len(scores))
print('표준편차 = ', round(std_s, 3))

max_ss = scores[0]
min_ss = scores[0]
for score in scores:
    if score > max_ss: # 리스트에서 현재보다 큰 값은 찾으면
        max_ss = score # max_ss에 넣어라
    if score < min_ss: # 리스트에서 현재보다 작은 값을 찾으면
        min_ss = score # min_ss에 넣어라
print('최소 점수 = ', min_ss)
print('최대 점수 = ', max_ss)

# Cf) 정렬 함수
sorted_scores = sorted(scores)
print(sorted_scores) # scores 리스트가 정렬됨.(오름차순)
sorted_min = sorted_scores[0] # 0 번지(가장 낮은 점수)
sorted_max = sorted_scores[9] # 9 번지(가장 높은 점수)
print(sorted_min, sorted_max)