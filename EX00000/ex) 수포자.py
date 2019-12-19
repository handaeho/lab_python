def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    hits = [0, 0, 0]
    size = len(answers)
    for i in range(size):
        if answers[i] == p1[i%len(p1)]:
            hits[0] += 1
        if answers[i] == p2[i%len(p2)]:
            hits[1] += 1
        if answers[i] == p3[i%len(p3)]:
            hits[2] += 1

    max_score = max(hits)
    for x in range(len(hits)):
        if hits[x] == max_score:
            answer.append(x+1)
    return answer

print(solution([1,3,2,4,2]))