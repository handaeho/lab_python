# 19.11.05 Python Class 06
"""
문자열(str) 타입
"""
s = '한대호'
print(s)

# 이렇게도 만들수 있다.
t = '''
안녕하세요. 파이썬입니다.
잘 지내시죠?
'''
print(t)

r = """
반가워요. 파이썬.
잘 지냅니다.
"""
print(r)

# 줄바꿈(\n), tab(\t)
v = '\t안녕하세요!\n\t반가워요!'
print(v)
# 그런데 읽고 보기에 너무 불편. 따라서 위의 방법처럼 """ ~~~ """로 묶어서 쓰는게 편하다.

# 문자열 인덱스
ss = 'hello'
print(ss[0]) # 결과 h
print(ss[1]) # 결과 e
# 문자열의 인덱스는 0부터 시작. ss('hello')의 경우 0~4의 인덱스를 가지게 됨.

# 문자열 슬라이싱
# x:y ~~~> from x(x는 포함) to y(y는 미포함)
print(ss[0:2]) # 결과 he (인덱스 0, 1 출력)
print((ss[1:5])) # 결과 ello (인덱스 1, 2, 3, 4 출력)
print((ss[1:])) # 결과 ello. 시작 값만 주고 끝 값을 안주면, 그 배열의 끝까지 출력.
print(ss[:3]) # 결과 hel. 시작 값을 안주고 끝 값만 주면, 끝값 - 1 까지 출력.
print((ss[-4:-2])) # 결과 el



