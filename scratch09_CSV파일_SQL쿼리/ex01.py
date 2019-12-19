"""
import csv ~> csv 모듈을 통한 csv 파일 사용
"""
import csv

row1 = ['test1', 'success', 'Mon'] # 문자열 리스트
row2 = ['test2', 'failure, kind of', 'Mon'] # 문자열안에 ','가 들어감
row3 = ['test3', 'success, kind of', 'Mon'] # 문자열안에 ','가 들어감
result = [row1, row2, row3]
print(result)
# [['test1', 'success', 'Mon'], ['test2', 'failure, kind of', 'Mon'], ['test3', 'success, kind of', 'Mon']]

# csv 모듈을 import 하고 파일을 쓰기 모드로 열기
# newline='' 파라미터를 추가하면, 빈 문자열이 출력되지 않는다.
with open('test_result.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=',') # csv writer 객체 생성
    for row in result: # writer 객체의 writerow() 메소드를 사용해 한 줄씩 쓰기
        writer.writerow(row)
        # -> row1, 2, 3의 내용이 있는 'test_result.csv' 파일이 같은 경로에 생성됨.
        # test1,success,Mon
        # test2,"failure, kind of",Mon
        # test3,"success, kind of",Mon

        # delimiter=',' ~> 문자열 안의 ','는 구분자가 아닌 그냥 있는 기호로 취급됨
        # ','가 있는 문자열은 ""로 묶였고, 없으면 그냥 출력됨

print('\n csv 모듈을 사용하지 않는 경우')
# csv 모듈을 import 하지 않고, csv 파일을 읽었을 때의 문제점
with open('test_result.csv', mode='r', encoding='utf-8') as f:
    for line in f:
        print(line.strip().split(','))
        # ['test1', 'success', 'Mon']
        # ['test2', '"failure', ' kind of"', 'Mon']
        # ['test3', '"success', ' kind of"', 'Mon']
        # 'test_result.csv'에서 ','가 포함되어야 하는 문자열이 ','때문에 구분되어 버렸다.
        # 또한 원래 데이터에는 없어야 할 ""가 문자열에 포함되었다.

print('\n csv 모듈을 사용하는 경우')
# csv 모듈을 import 해, csv 파일을 읽었을 때
with open('test_result.csv', mode='r', encoding='utf-8') as f:
    # csv.reader 객체 생성
    reader = csv.reader(f)
    for row in reader: # reader 객체의 read 기능으로 한 줄씩 읽음
        print(row)
        # ['test1', 'success', 'Mon']
        # ['test2', 'failure, kind of', 'Mon']
        # ['test3', 'success, kind of', 'Mon']
        # ','가 포함된 문자열이 정상적으로 출력됨.
