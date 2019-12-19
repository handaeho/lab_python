"""
Function 연습 문제
"""
# 1.
# 1 ~ n까지의 합계를 리턴하는 함수
def sum_n(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)
sum_n(100)

# 2.
# 1 ~ n의 제곱의 합계를 리턴하는 함수
def sum_nn(n):
    total = 0
    for i in range(n+1):
        total += i ** 2
    print(total)
sum_nn(3)

# 3.
# 숫자들의 리스트를 전달받아 최대값을 찾아 리턴하는 함수
def max_n(n):
    for i in range(len(n)-1):
        max = i
        for j in range(i+1, len(n)):
            if n[max] < n[j]:
                max = j
        n[i], n[max] = n[max], n[i]
    return n[0]
print(max_n([1, 5, 3, 6, 9, 10, 100, 2, 80]))

# 4.
# 숫자들의 리스트를 전달받아 최대값의 인덱스를 리턴하는 함수
def max_index(n : list):
    # max_i = n[0]
    # for i in n:
    #     if i > max_i:
    #         max_i = i
    # return n.index(max_i)

    max_id, max_val = 0, n[0]
    for i, v in enumerate(n): # 리스트의 순서(index)와 값을 전달하는 함수.
        print(f'i = {i}, v = {v}')
        if v > max_val:
            max_id, max_val = i, v
    return max_id
print(max_index([1, 5, 3, 6, 9, 10000, 100, 2, 80,1000]))

# 5.
# 숫자들의 리스트를 전달 받아, 중앙값을 리턴하는 함수
def mid_n(n : list):
    import math
    a = sorted(n)
    x = len(n)
    if x % 2 == 0: # 리스트 개수가 짝수
        mid = (a[int(x/2) - 1] + a[int(x/2)]) / 2
    elif x % 2 == 1: # 리스트 개수가 홀수
        mid = a[math.ceil(x/2) - 1]
    return mid
print(mid_n([1, 3, 5, 9]))

# sorted(list) => 리스트를 정렬한 새로운 리스트를 리턴. 원본 리스트는 변화 X.
# list.sort() => 원본 리스트를 정렬해 저장. 리턴 값은 None(없음).
# 그래서 list.sort()를 원본 리스트에 저장해버리면, 원본 리스트는 None로 바뀌어 날아가버림.

