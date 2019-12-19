def solution(n):
    answer = ''
    while n:
        n, na = divmod(n, 3)
        answer = '412'[na] + answer
        if not na:
            n -= 1
    return answer


print(solution(10))