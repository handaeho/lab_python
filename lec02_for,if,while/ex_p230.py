# 13.
for i in range(1, 8):
    for j in range(1, i+1):
        print('T', end='')
    print()

# 14.
print('----------------------')
for i in range(1, 8):
    for j in range(1, 8-i):
        print(' ', end='')
    for j in range(1, i+1):
        print('T', end='')
    print()
# 15.
print('----------------------')
i = 1
while i <= 7:
    j = 1
    while j <= i:
        print('T', end='')
        j += 1
    i += 1
    print()

print('----------------------')
width = 1
while width < 8:
    print(' ' * (7 - width), 'T' * width, sep='')
    width += 1
# 16.
print('----------------------')
rat_1_weight = []
rat_2_weight = 100
rat_1_rate = 0.04
rat_2_rate = 0.02
week = 1
while rat_1_weight[week] / rat_1_weight[0] - 1 < 0.25:
    week += 1
print(week)

