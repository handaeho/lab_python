def solution(s):
    answer = 0
    min = 99999999
    if len(s) == 1:
        return 1
    for size in range(1, int(len(s)/2) + 1):
        cnt = 0
        before = ''
        for i in range(0, len(s)+1, size):
           if before[-size:] == s[i:i+size]:
               cnt += 1
           else:
               if cnt > 1:
                   before += str(cnt)+s[i:i+size]
               else:
                   before += s[i:i+size]
               cnt = 1
        if min > len(before):
            min = len(before)
    answer = min
    return answer

print(solution('ababcdcdababcdcd'))