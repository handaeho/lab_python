def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if answer.__len__() == 0:
        answer = [-1]
    return sorted(answer)

print(solution([3, 2, 6], 10))
print(solution([5, 9, 7, 10], 5))
