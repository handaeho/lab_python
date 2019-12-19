"""
Class 사용 예
"""
s = 'hello'
print(type(s)) # <class 'str'>
print(s.capitalize()) # Hello ~~~> 첫 글자를 대문자로
print(s.upper()) # HELLO ~~~> 모든 글자를 대문자로
print(s.find('l')) # 2 ~~~> 해당 문자의 위치를 찾음

s2 = 'python'
print(type(s2)) # <class 'str'>
print(s2.capitalize()) # Python ~~~> 첫 글자를 대문자로
print(s2.upper()) # PYTHON ~~~> 모든 글자를 대문자로
print(s2.find('l')) # -1 ~~~> 해당 문자의 위치를 찾음(-1 ~> 없음)
