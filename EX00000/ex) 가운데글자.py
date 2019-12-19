def solution(s):
    length = len(s)
    if length % 2 == 1:
        answer = str(s[(length//2)])
    else:
        answer = str(s[(length//2)-1]) + str(s[(length//2)])
    return answer

print(solution(['q', 'w', 'e', 'r', 't']))
