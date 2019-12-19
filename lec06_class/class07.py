class Account:
    """
    은행 계좌 클래스

    field(데이터): 계좌번호(accountno), 잔액(balance)
    method(기능): 입금(deposit), 출금(withdraw), 이체(transfer)
    """
    def __init__(self, accountno, balance):
        self.accountno = accountno
        self.balance = balance
        # isinstance(balance, int) ==> balance가 int형이냐? ~~~> True / False 반환
        if not isinstance(balance, int) and not isinstance(balance, float):
            raise TypeError(' ')


        # 또는 이렇게도 가능하다.
        # try:
        #     temp = balance + 1 ~~~> temp는 실제로는 안 쓰이는 '임시 변수'. 선언 없이 쓰일수 있다.
        # except Exception:
        #     raise TypeError()

    def __repr__(self): # __repr__ ~~~> 문자열을 반환
        return f'계좌 번호 : {self.accountno}, 잔액 : {self.balance}원'


    def deposit(self, price): # 입금
        if price < 0:
            raise ValueError('입금 금액은 0원 이상이어야 합니다.')

        self.balance += price
        print(f'고객님의 계좌 {self.accountno}에 금 {price}원이 입금 되었습니다.')
        print(f'현재 잔액은 {self.balance}원 입니다.')

    def withdraw(self, price): # 출금
        self.balance -= price
        print(f'고객님의 계좌 {self.accountno}에서 금 {price}원이 출금 되었습니다.')
        print(f'현재 잔액은 {self.balance}원 입니다.')


    def transfer(self, to, price): # 송금
        """
        상대방에게 송금하기 또는 송금 받기
        :param to: 상대방
        :param price: 송금 금액
        :return: None
        """
        self.withdraw(price) # 내 계좌에서 출금. 즉, 상대방(to)에게 송금.
        to.deposit(price) # 내 계좌로 입금. 즉, 상대방(to)이 송금.

# 생성자 호출
if __name__ == '__main__': # main문(실행문)
    account1 = Account(95679859539, 10000000)
    print(account1)

    account2 = Account(123456789, 100)
    print(account2)

    account1.deposit(10000)
    account1.withdraw(500000)

    account2.deposit(100000)
    account2.withdraw(30000)

    account1.transfer(account2, 10000) # account1이 account2에게 10000원 송금
    account2.transfer(account1, 100) # account2가 account1에게 100원 송금

