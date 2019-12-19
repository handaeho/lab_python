"""
dictionary comprehension
"""
numbers = [1, 2, 3, 4, 5]
names = ['a', 'b', 'c', 'd', 'e']

students = {} # empty dict
for i in range(len(numbers)):
    students[numbers[i]] = names[i]
print(students) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

students2 = {numbers[i] : names[i] for i in range(len(numbers))}
print(students2) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# zip() = 리스트 두개를 묶는다.
num_name = zip(numbers, names)
print(num_name) # <zip object at 0x000001989E222B48>
for x in num_name:
    print(x, end=' ') # (1, 'a') (2, 'b') (3, 'c') (4, 'd') (5, 'e')
print()

students3 = {}
for key, value in zip(numbers, names):
    students3[key] = value
print(students3) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

students4 = {key : value for key, value in zip(numbers, names)}
print(students4) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

students5 = {key : value for key, value in zip(numbers, names)
             if key % 2}
print(students5) # {1: 'a', 3: 'c', 5: 'e'} (1:True, 0:False)