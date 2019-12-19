"""
반복문 - for문
Iterable Type(반복가능한 타입) = list, tuple, dict, str(문자열) 등

for 변수 in Iterable Type:
    반복할 문장들
"""
# range(to) : 0부터 to-1까지 범위의 숫자들
# range(from, to) : from부터 to-1까지 범위의 숫자들
# range(from, to, step) : from부터 to-1까지 step만큼씩 증가 혹은 감소

for i in range(5):
    print(i, end=' ')
print()  # 0 1 2 3 4

for i in range(1, 5):
    print(i, end=' ')
print()  # 1 2 3 4

for i in range(1, 10, 2):
    print(i, end=' ')
print()  # 1 3 5 7 9

for s in 'Hello, Python!':
    print(s, end=' ')
print()  # H e l l o ,   P y t h o n !

languages = ['PL/SQL', 'R', 'Python', 'Java']
for lang in languages:
    print(lang, end=' ')
print()  # PL/SQL R Python Java

for i in range(len(languages)):
    print(i, languages[i], end=' ')
print()  # 0 PL/SQL 1 R 2 Python 3 Java

alphbet = {1: 'a', 2: 'b', 3: 'c'}
print(alphbet.keys())   # dict keys
for key in alphbet.keys():
    print(key, alphbet[key], end=' ')
print()  # 1 a 2 b 3 c

# item = (key, value)
for item in alphbet.items():
    print(item, end=' ')
print()  # (1, 'a') (2, 'b') (3, 'c')

# key, value = (1, 'a'), (2, 'b'), ...처럼 decomposition하는 것도 가능
for key, value in alphbet.items():
    print(key, value, end=' ')
print()  # 1 a 2 b 3 c

