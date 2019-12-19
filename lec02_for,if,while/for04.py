# for - in

# Cf) break / continue

for i in range(1, 10):
    if i == 5:
        break # 결과 1 2 3 4 -> 5에서 for문 종료.
    print(i, end=' ')
print()

for i in range(1, 10):
    if i == 5:
        continue # 결과 1 2 3 4 6 7 8 9 -> 5에서 for문 시작으로 돌아감.
    print(i, end=' ')
print()

# =====================================================================

# 피보나치 수열
f = [0, 1]
x = int(input('피보나치 수열 >>> '))
for i in range(2, x+1):
    f.append(f[i-1] + f[i-2])
print(f)

# =====================================================================

# Prime Number(소수)
prime = int(input('Prime Number >>> '))
for i in range(2, prime):
    ck = True
    for j in range(2, i):
        if i % j == 0:
            ck = False
            break
    if ck:
        print(i, end=' ')
        print()

# =====================================================================

# for / while문(반복문)과 else가 함께 사용되는 경우
# 반복문이 break 를 만나지 않고, 범위 전체를 반복하면 else 실행.
# 반복문 중간에 break를 만나면, else는 실행 안됨.
for i in range(5):
    if i == 3:
        break
    print(i, end=' ')
else:
    print('반복문 정상 종료') # 현재 break를 만나 else 구문 실행 X
print()

# for ~ else를 사용한 Prime Number
for n in range(2, 11):
    for divider in range(2, n):
        if n % divider == 0:
             break # 소수가 아니다. (1과 자신 외에 나누어 떨어지는 수가 있다.)
    else: # break를 만나지 않았을때, 실행되는 else 구문.
        print(f'{n}은 Prime Number')

