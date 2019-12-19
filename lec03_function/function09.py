"""
재귀 함수(Recursive function) : 자기 자신을 함수 내에서 호출하는 함수

단, 끝나는 시점 없이 계속해서 재귀하게 되면, 무한 루프에 빠진다.(Stack over flow 발생)
그러나, 파이썬에서는 재귀함수를 이용한 반복에 제한이 있어(최대 깊이), 초과하면 강제 종료 된다.
(RecursionError: maximum recursion depth exceeded while calling a Python object)
"""
# n! = 1 x 2 x 3 x ... x n-1 x n = (n-1)! x n ---> 여기서 '재귀'. 팩토리얼을 계산하는 공식에 팩토리얼이 쓰인다.
def fact(n : int) -> int:
    # for문을 이용한 팩토리얼
    fact_n = 1
    for i in range(1, n+1):
        fact_n *= i
    return fact_n

def fact_recur(n : int) -> int:
    if n == 0:
        return 1 # 재귀 종료 조건
    elif n > 0:
        return fact_recur(n-1) * n # 재귀. fact_recur 안에서 fact_recur를 호출


for i in range(6):
   print(f'{i}! = {fact(i)}')

print('============================')

for i in range(6):
    print(f'{i}! = {fact_recur(i)}')

print('============================')

# '하노이의 탑'문제를 재귀 함수로 풀어보자
def hanoi(n, start, target, sub): # a에서 c를 거쳐 b로간다(최종 목표)
    """
    재귀 함수를 이용한 하노이의 탑
    :param n: 옮길 원반의 개수(n>0, n은 정수)
    :param start: 원반들이 있는 시작 기둥
    :param target: 원반들이 모두 옮겨질 목표 기둥
    :param sub: 원반들을 옮길때 사용할 보조 기둥
    :return: None
    """
    if n == 1:
        print(f'{start}에서 {target}으로 {n}번째 원판을 옮김.')
        return # 함수 종료
    else:
        hanoi(n-1, start, sub, target)
        # n-1개의 원반을 target 기둥을 보조 역할로 사용해, sub 기둥으로 옮김.
        print(f'{start}에서 {target}으로 {n}번째 원판을 옮김.')
        hanoi(n-1, sub, target, start)
        # sub 기둥에 남아있는 n-1개의 원반을 start 기둥을 보조 역할로 사용해 target 기둥으로 옮김.
        return

print(hanoi(5, 'a', 'b', 'c')) # 이 함수가 반복되면서, start, sub, target은 계속 변한다.
# 하노이의 탑 공략
# 원반 수가 '홀수'일때는 맨 위의 원반을 '목표 기둥'에 먼저 놓고,
# 원반 수가 '짝수'일때는 맨 위의 원반을 '목표 기둥이 아닌 보조 기둥'에 먼저 놓는다.





