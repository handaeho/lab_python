"""
tuple 타입의 단점
    - 해당 인덱스의 원소가 어떤 값을 의미 하는지 파악하기 힘듦.
    - 특정 원소에 접근(read/write)하기 위해서는 인덱스만 사용해야 함.

이러한 단점들을 해결하기 위해, 튜플의 특징과 dict의 특징을 모두 갖는 'NamedTuple' 클래스가 있다.
    - NamedTuple : 튜플의 이름과 원소들의 label를 모두 지정해 주어야 한다.
"""
from collections import namedtuple
from typing import NamedTuple


# Tuple Ver.
# 번호, 이름, 수학 점수, 과학 점수, 컴퓨터 점수

student_1 = (1, '홍길동', 10, 20, 30)
print('번호 : ', student_1[0])
print('과학 점수 : ', student_1[3])

# NamedTule Ver.
student_namedtuple = namedtuple('student', ('no', 'name', 'math', 'science', 'cs'))
# ~> student라는 튜플에 'no', 'name', 'math', 'science', 'cs'라는 레이블을 갖는 원소들을 만든다.(like dict)
student_2 = student_namedtuple(3, '허균', 100, 100, 100) # 이렇게 함수처럼 불러와서 쓸 수 있다.
print(student_2)
print(f'점수 index ver. : {student_2[0]}, 점수 label ver. : {student_2.no}')
print(f'점수 index ver. : {student_2[2]}, 점수 label ver. : {student_2.math}')
print(f'점수 index ver. : {student_2[0]}, 점수 label ver. : {student_2.science}')

# Python 3.6 이상부터 NamedTuple을 class처럼 선언하는 방식이 만들어졌다.
class Student2(NamedTuple): # NamedTuple 패키지 import 필요.
# ~> Student2  클래스는 NameTuple 클래스를 상속받는다.
     # field 선언 - 변수 타입 annotation을 반드시 추가해야 함.(반드시 사용할 label과 각 타입 선언)
     no: int
     name: str
     math: int
     science: int
     cs: int


student_3 = Student2(4, 'abc', 90, 88, 77) # 만든 Student2 클래스 생성자 호출 및 할당
print(student_3) # Student2(no=4, name='abc', math=90, science=88, cs=77)


