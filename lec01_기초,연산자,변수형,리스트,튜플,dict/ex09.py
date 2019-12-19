# 19.11.05 Python Class 09
"""
dict : key와 value의 쌍으로 이루어진 데이터를 저장하는 사전(dictionary)식 데이터 타입. 중괄호{}를 사용.
"""
person = {'name': '대호', 'age': 26, 'height': 500}
print(person) # 결과 {'name': '대호', 'age': 26, 'height': 500}
print(type(person)) # 결과 <class 'dict'>
# key / value는 어떤 타입이던지 사용가능. 중복만 되지 않으면 된다.

# dict의 데이터 참조. 인덱스 자리에 key를 넣어준다.
print(person['name'])
print(person['age'])
print(person['height'])
print(person.keys()) # dict_keys(['name', 'age', 'height'])
print(person.values()) # dict_values(['대호', 26, 500])
print(person.items()) # dict_items([('name', '대호'), ('age', 26), ('height', 500)])
# items = (key, value)를 알아낼 때.
# items는 ()와 []로 묶임. 즉, 튜플들로 이루어진 리스트 형태.

student = {1: '강다혜', 2: '김수인', 3: '김영광', 10: '안도연'}
print(student[1])
print(student[2])
print(student[3])
# 인덱스를 사용한것 같지만, student dict는 key로 1, 2, 3을 사용했다.

# dict에 원소를 추가하고자 한다면
student[4] = '김재성'
print(student) # {1: '강다혜', 2: '김수인', 3: '김영광', 10: '안도연', 4: '김재성'}

# dict의 원소를 변경하고자 한다면
student[4] = '김재성님'
print(student) # {1: '강다혜', 2: '김수인', 3: '김영광', 10: '안도연', 4: '김재성님'}

# dict의 원소를 삭제하고자 한다면
student.pop(4) # pop(key 값)
print(student) # {1: '강다혜', 2: '김수인', 3: '김영광', 10: '안도연'}

book = {
    'title': 'python programming book',
    'authors': ['제니퍼', '폴', '제이슨'],
    'company': '길벗',
    'isbn': 97911
}
print(book)
# {'title': 'python programming book', 'authors': ['제니퍼', '폴', '제이슨'], 'company': '길벗', 'isbn': 97911}
print(book['authors']) # ['제니퍼', '폴', '제이슨']
print(book['company']) # 길벗
print(book['authors'][0]) # 제니퍼
