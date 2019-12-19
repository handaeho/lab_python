"""
Class 연습(클래스 생성, 인스턴스 / 메소드 생성 및 사용)
"""
class Employee:
    """
    Field ~> empno, ename, sal, deptno
    Method ~> 급여 인상률을 받아 인상된 급여 리턴
    """
    def __init__(self, empno, ename, deptno, sal):
        self.empno = empno
        self.ename = ename
        self.deptno = deptno
        self.sal = sal

    def rasie_salary(self, pct):
        return self.empno, self.ename, self.deptno, self.sal + (self.sal * pct)


emp1 = Employee(1, '김철수', 10, 1000)
print(emp1.rasie_salary(0.15))
