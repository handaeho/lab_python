# Iterable: for-in 구문에서 사용할 수 있는 타입들
#   list, tuple, set, dict, numpy.ndarray, pandas.DataFrame, ...
#   for x in list: ...

a = [1, 3, 0, 9, -1]
result = sorted(a, key=lambda x: -abs(x))
print(f'a={a}, result={result}')

result = a.sort()
print(f'a={a}, result={result}')


b = ['cat', 'bb', 'dogs', 'apple']
result = sorted(b, key=lambda x: len(x))
print(f'b={b}, result={result}')

c = {'cat': 10, 'bb': -1, 'dogs': 3, 'apple': 5}
for x in c: # 이런 구문은 key만이 출력됨
    print(x)
    # cat
    # bb
    # dogs
    # apple

for x in c.items(): # 이런 구문은 (key: value) 튜플을 출력
    print(x)
    # ('cat', 10)
    # ('bb', -1)
    # ('dogs', 3)
    # ('apple', 5)

result = sorted(c)
# dict의 '키'를 알파벳 순서로 정렬한 리스트
print(f'c={c}, result={result}')
# c={'cat': 10, 'bb': -1, 'dogs': 3, 'apple': 5}, result=['apple', 'bb', 'cat', 'dogs']

result2 = sorted(c, key=lambda x: len(x))
# ~~~> x에 c가 전달되어 x의 길이. 즉, 키의 길이로 정렬하는 lambda를 적용
print(f'c={c}, result={result2}')
# c={'cat': 10, 'bb': -1, 'dogs': 3, 'apple': 5}, result=['bb', 'cat', 'dogs', 'apple']

result3 = sorted(c.values())
# ~~~> x의 values. 즉, values를 정렬
print(f'c={c}, result={result3}')
# c={'cat': 10, 'bb': -1, 'dogs': 3, 'apple': 5}, result=[-1, 3, 5, 10]

result4 = sorted(c.values(), key=lambda x: abs(x))
# ~~~> x의 values의 절대값. 즉, values의 절대값으로 정렬하는 lambda를 적용
print(f'c={c}, result={result4}')
# c={'cat': 10, 'bb': -1, 'dogs': 3, 'apple': 5}, result=[-1, 3, 5, 10]

result5 = sorted(c.items())
# ~~~> dict의 (key:values) 튜플을 정렬. 정렬 기준은 key
print(f'c={c}, result={result5}')
# c={'cat': 10, 'bb': -1, 'dogs': 3, 'apple': 5}, result=[('apple', 5), ('bb', -1), ('cat', 10), ('dogs', 3)]

result6 = sorted(c.items(), key=lambda x: len(x[0]))
# ~~~> x에 dict의 (key:values) 튜플이 전달되고, 튜플의 0번지인 key의 len으로 정렬
print(f'c={c}, result={result6}')
# c={'cat': 10, 'bb': -1, 'dogs': 3, 'apple': 5}, result=[('bb', -1), ('cat', 10), ('dogs', 3), ('apple', 5)]

result7 = sorted(c.items(), key=lambda x: x[1])
# ~~~> x에 dict의 (key:values) 튜플이 전달되고, 튜플의 1번지인 value로 정렬
print(f'c={c}, result={result7}')
# c={'cat': 10, 'bb': -1, 'dogs': 3, 'apple': 5}, result=[('bb', -1), ('dogs', 3), ('apple', 5), ('cat', 10)]

# sorted는 class 타입도 정렬할 수 있다!
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(이름 : {self.name}, 나이 : {self.age})'


p1 = Person('이지수', 10) # 생성자 호출
print(p1.name, p1.age) # field = property(특성, 속성) = member variable(멤버 변수) ~~~> 클래스가 갖고 있는 변수
p2 = Person('심진섭', 20) # 생성자 호출
p3 = Person('조성우', 30) # 생성자 호출

persons = [p1, p2, p3]
print(persons)
# [Person(이름 : 이지수, 나이 : 10), Person(이름 : 심진섭, 나이 : 20), Person(이름 : 조성우, 나이 : 30)]

result = sorted(persons, key=lambda x: x.name)
# ~~~> x에 p1, p2, p3가 전달된다. 즉, 참조 변수 x는 persons 리스트가 되는 것. 그리고 그 리스트의 변수가 정렬의 기준.
print(result)
# [Person(이름 : 심진섭, 나이 : 20), Person(이름 : 이지수, 나이 : 10), Person(이름 : 조성우, 나이 : 30)]
