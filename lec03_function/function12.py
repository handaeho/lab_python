"""
함수에서 'return'의 의미
1) 함수의 종료
2) 함수를 호출한 곳에 값을 반환

yield : 반복문 안에서만 함수의 결과를 순차적으로 리턴할 때 사용.
값을 가지고 있다가 반복 될 때마다 하나씩 하나씩 리턴함.
따라서, yield를 이용한 결과 값을 보려면, 반목문을 사용해 출력해야한다.
"""
def test():
    x = 0
    while x < 4:
        return x # 여기서 이 test() 함수는 종료됨.(결과값을 리턴하므로)
        x += 1 # 따라서 이 연산은 실행 될 수 없음.

for i in range(4):
    print(test()) # 0 0 0 0 ~~~> 'x += 1'은 실행 X

def four():
    x = 0
    while x < 4:
        yield x
        x += 1

print(four()) # <generator object four at 0x000002458ED857C8>
# x가 아닌 'generator'을 리턴한다.

for x in four(): # 함수 안의 변수인 x 전달. ~~~> 리턴 값도 x가 됨.
    print(x) # 0 1 2 3
# 이 for 반복문 안에서만 yield는 x를 가지고 있다가, for문이 한번 돌때마다 x를 리턴함.

print(range(4)) # range(0, 4) ~~~> range() 역시 일종의 generator. yield를 사용하고 있음.

def my_range(start=0, end=1):
# 첫번째 파라미터가 default 값을 가지면, 뒤의 파라미터들도 default를 가져야함
    x = start
    while x < end:
        yield x
        x += 1

print(my_range()) # <generator object my_range at 0x000001F4ED2857C8>

for x in my_range(start=1, end=5):
    print(x) # 1 2 3 4


