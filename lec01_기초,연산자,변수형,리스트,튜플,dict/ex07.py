# 19.11.05 Python Class 07
"""
리스트(list) : 여러개의 값들을 하나의 변수에 저장하기 위한 데이터 타입.
원소(element) = 리스트에 저장된 값.
인덱스(index) = 리스트에 값이 저장된 위치(번호).
리스트 원소들은 추가 및 삭제, 변경이 가능하다.(mutable)
"""
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])
print(numbers[4])
# print(numbers[5]) ---> 인덱스는 4번까지만 존재.
print(numbers[0:3])

# 원소 변경하기
numbers[0] = 1000
print(numbers) # 결과 [1000, 2, 3, 4, 5]

# 원소 추가하기
numbers.append(5050)
print(numbers) # 결과 [1000, 2, 3, 4, 5, 5050]
# append는 값을 하나만 추가할 수 있다.(append = 붙이다)
numbers.extend([9, 8, 7])
print(numbers) # 결과 [1000, 2, 3, 4, 5, 5050, 9, 8, 7]
# extend는 여러개를 추가할 수 있다.(extend = 확장)

# append에 [10, 11, 12]를 쓰면?
numbers.append([10, 11, 12])
print(numbers) # 결과 [1000, 2, 3, 4, 5, 5050, 9, 8, 7, [10, 11, 12]]
# 리스트 [10, 11, 12] 자체를 하나의 원소로 추가한다.

# 원소 삭제
numbers.remove(1000)
print(numbers) # 결과 [2, 3, 4, 5, 5050, 9, 8, 7, [10, 11, 12]]
# remove = 원소 값을 사용해서 삭제.
del numbers[1]
print(numbers) # 결과 [2, 4, 5, 5050, 9, 8, 7, [10, 11, 12]]
# del = 원소의 인덱스를 사용해서 삭제.

# 비어있는 리스트 생성
empty = []
print(empty)

# 파이썬의 리스트는 여러가지 타입의 값들을 함께 저장할 수 있다.
person = ['대호', 26, 1994, '일산']
print(person) # 결과 ['대호', 26, 1994, '일산']
print(person[0], type(person[0])) # 결과 대호 <class 'str'>
print(person[2], type(person[2])) # 결과 1994 <class 'int'>

# List Decomposition(리스트 분해)
name, age, birth, addr = person
print(name, age, birth, addr)
# 결과 대호 26 1994 일산
# 선언한 각 변수에 person 리스트의 각 원소들을 저장한다.

# 2차원 리스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix) # 결과 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0], type(matrix[0])) # 결과 [1, 2, 3] <class 'list'>
# matrix의 크기는 3, 원소의 수는 3개가 된다.
# [1, 2, 3] / [4, 5, 6] / [7, 8, 9] 각 리스트가 원소가 되는 것
print(matrix[0][0]) # 결과 1
print(matrix[0][1]) # 결과 2
print(matrix[1][2]) # 결과 6
print(matrix[0:2]) # 결과 [[1, 2, 3], [4, 5, 6]]

