# 19.11.05 Python Class 08
"""
튜플(tuple) : 원소(값)들을 변경 할 수 없는 리스트. 대괄호[]가 아닌 소괄호()를 사용한다.
"""
number = (1, 2, 3)
print(number)
print(number[0])
print(number[0:2])
one, two, three = number
print(one, two, three)
# 리스트와 같이 인덱스, 슬라이싱, decomposition 모두 가능하다.

# 그러나 튜플내의 원소들을 변경할 수는 없다.
# number[0] = 100
# print(number) # 에러 발생. TypeError: 'tuple' object does not support item assignment
# 마찬가지로 append, extend 역시 불가능하다.
