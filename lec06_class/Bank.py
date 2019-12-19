"""
lec06_class\class07.py에서 작성한 Account 클래스를 사용해 은행 APP을 만들어 보자

1) 계좌 개설 / 2) 입금 / 3) 출금 / 4) 이체의 기능을 가진 APP 설계.
"""
from lec06_class.class07 import Account

print('인민 은행 Application')

accounts = {}
# 여러개의 계좌를 관리하기 위한 dict (key: 계좌번호, value: Account 객체) ~~~> 전역 변수

while True:
    # 메인 메뉴
    print('[0] 종료 [1] 계좌 개설 [2] 입금 [3] 출금 [4] 이체 [5] 계좌 정보')
    menu = int(input('기능을 골라주세요! >>> '))
    print('-------------------------------------------------')

    if menu == 0:
        print('어플을 종료합니다...')
        break

    elif menu == 1: # 계좌 개설
        print('신규 계좌 개설을 환영합니다.')
        print('원하는 계좌를 입력하세요 >>> ')
        account_no = int(input())
        print('얼마로 시작 하겠습니까? >>> ')
        money = int(input())

        accounts[account_no] = Account(account_no, money) # import된 class07의 Account 클래스
        # accounts 딕셔너리에 account_no를 key로, Account 객체 자체를 value로
        print('완료되었습니다.')
        print(f'계좌 번호는 {account_no} / 잔액은 {money}입니다.')
        print(accounts)
        # {123456: 계좌 번호 : 123456, 잔액 : 1000원} ~~~> {key(123456): value(나머지 쭉)}
        # {789000: 계좌 번호 : 789000, 잔액 : 100원} ~~~> {key(789000): value(나머지 쭉)}
        print('-------------------------------------------------')

    elif menu == 2: # 입금
        print('입금을 선택 하셨습니다.')
        account_no = int(input('입금할 계좌 번호를 입력해 주세요 >>> '))
        money = int(input('입금할 금액을 입력해 주세요 >>> '))
        accounts[account_no].deposit(money) # Account 클래스의 deposit 메소드 사용
        print('-------------------------------------------------')

    elif menu == 3:
        print('출금을 선택하셨습니다.')
        account_no = int(input('출금할 계좌 번호를 입력해 주세요 >>> '))
        money = int(input('출금할 금액을 입력해 주세요 >>> '))
        accounts[account_no].withdraw(money) # Account 클래스의 withdraw 메소드 사용
        print('-------------------------------------------------')

    elif menu == 4:
        print('이체를 선택하셨습니다.')
        from_acc = int(input('어느 계좌에서 이체 하시겠습니까? >>> '))
        to_acc = int(input('이체할 계좌 번호를 입력해 주세요 >>> '))
        money = int(input('이체할 금액을 입력해 주세요 >>> '))
        accounts[from_acc].transfer(accounts[to_acc], money) # Account 클래스의 transfer 메소드 사용
        # 보내는 계좌(from_acc)와 받는 계좌(to_acc) 두 개를 accounts 딕셔너리에서 key로 찾아야한다.
        print('-------------------------------------------------')

    elif menu == 5: # 계좌 정보
        account_no = int(input('조회할 계좌를 입력하세요. >>> '))
        print(accounts[account_no])
        # 조회할 계좌를 입력하세요. >>> 123456
        # 계좌 번호 : 123456, 잔액 : 1000원
        print('-------------------------------------------------')