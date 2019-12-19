def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = []
    n = 0
    for i in range(0, 12):
        n += days[i]
        total_days.append(n)

    Q_day = total_days[a-1] + b
    w_day = Q_day % 7

    answer = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'][w_day+1]

    return answer


print(solution(5, 24))