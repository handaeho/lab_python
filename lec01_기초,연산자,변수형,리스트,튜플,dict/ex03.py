# 19.11.04 Python Class 03
"""
파이썬 데이터 타입
숫자 타입 -> int(정수) / float(실수) / complex(복소수)
문자 타입 -> str
논리 타입 -> bool(True / False)
시퀸스(sequence) -> list / tuple
매핑(mapping) -> dict
집합 -> set
None -> '값이 없음'을 나타내는 데이터 타입
"""
# -----------------------------------------------------------------------------
intVal =123
floatVal = 3.141592
complexVal = 1 + 2j # j : 허수

print(type(intVal))
print(type(floatVal))
print(type(complexVal))
# 결과 ~~~~~> 변수의 타입
# <class 'int'> / <class 'float'> / <class 'complex'>

print(id(intVal))
print(id(floatVal))
print(id(complexVal))
# 결과 ~~~~~> 메모리 주소
# 140719357067344 / 2269695406864 / 1828809655504
# -----------------------------------------------------------------------------
name = 'abc'

print(type(name))
# 결과 <class 'str'>
# -----------------------------------------------------------------------------
result = 10 > 2

print(type(result))
# 결과 <class 'bool'>
print(result)
# 결과 True
# -----------------------------------------------------------------------------


