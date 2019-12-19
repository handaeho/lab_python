def solution(d, budget):
    d = sorted(d)
    total = 0
    cnt = 0
    for i in range(len(d)):
        total += d[i]
        if total > budget:
            break
        cnt += 1

    answer = cnt
    return answer

print(solution([2,2,3,3], 10))