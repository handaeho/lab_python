"""
반복문 연습
shift + F6 ~~~> Refactor / Rename(해당 변수 이름 전부 바꾸기)
"""
# 1 + 2 + 3 + ... + 99 + 100?
n = 1
sum = 0
while n < 101:
    sum = sum + n
    n += 1
print(sum)  # 5050

# 1 + 2 + 3 + ... + n <= 100?
n = 0
sum = 0
while sum + n <= 100:
# sum <= 100으로 하면 sum은 104가 나온다.
# 그 이유는 n = 13, sum = 91에서 n++로 n = 14가 되었지만, 그때 sum은 91이어서 더해지고 sum = 104 상태로 while문이 종료되기 때문.
# 따라서 sum + n <= 100으로 먼저 n을 더해주어야 정상 종료 가능.
    n += 1
    sum = sum + n
    print(n, sum)  # 13 91
