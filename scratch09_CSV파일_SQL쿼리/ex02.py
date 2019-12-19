"""
csv 모듈을 사용한 mpg.csv 파일 읽기
"""
import csv
import os

file_path = os.path.join('..', 'scratch08_경사하강법', 'mpg.csv')
# Window : ..\scratch08_경사하강법\mpg.csv
# Linux, Mac : ../scratch08_경사하강법/mpg.csv
with open(file_path, mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    reader.__next__() # 한 줄 읽고 전너 뛰기 ~> 1번 줄은 컬럼 이름이므로 건너뜀
    df = [line for line in reader]

print(df[0:5])
# [['1', 'audi', 'a4', '1.8', '1999', '4', 'auto(l5)', 'f', '18', '29', 'p', 'compact'], ...
print(df[0][0], df[0][1], df[0][2], df[0][3])
# # df 리스트에서 0번째 행의 0, 1, 2, 3번째 컬럼 아이템만 출력 ~~~> 1 audi a4 1.8

# df 리스트에서 각 행마다 반복하면서, 각 행의 인덱스 아이템을 float형으로 새로운 리스트에 저장
displ = [float(row[3]) for row in df] # df의 row의 3번지 값들을 꺼내 float형으로 displ에 저장
cty = [float(row[8]) for row in df] # df의 row의 8번지 값들을 꺼내 float형으로 cty에 저장
print(displ)
print(cty)

# mpg.csv에는 컬럼 이름이 있다. ~~~> dict 형으로 읽어오기(key : value)
with open(file_path, mode='r', encoding='utf-8') as f:
    # dict(사전) 타입으로 데이터를 읽어주는 reader 객체
    # 보통 csv 파일에 컬럼이름이 포함된 경우 사용
    reader = csv.DictReader(f)
    df = [row for row in reader]

print(df[0:5])
# [OrderedDict([('', '1'), ('manufacturer', 'audi'), ('model', 'a4'), ('displ', '1.8'), ('year', '1999'), ...
print(df[0])
# OrderedDict([('', '1'), ('manufacturer', 'audi'), ('model', 'a4'), ('displ', '1.8'), ('year', '1999'), ...
print(df[0]['manufacturer']) # audi
print(df[0]['model']) # a4
print(df[0]['displ']) # 1.8
# ~> 0번째 인덱스의 행에 있는 컬럼 이름과 일치하는 값을 출력 해준다.
# 즉, 컬럼이름을 key 값으로 하여 그 key에 해당하는 value를 출력

displ = [float(row['displ']) for row in df] # key가 'displ'인 value 값을 float형으로 dipl에 저장
cty = [float(row['cty']) for row in df] # key가 'cty'인 value 값을 float형으로 dipl에 저장
# ~> 컬럼 이름을 key로 vaule를 찾을 수 있어, 인덱스를 이용하는 것보다 편하다.
print(displ)
print(cty)
