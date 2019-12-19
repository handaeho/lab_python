"""
Class = 데이터(필드) + 기능(메소드) ~~~> 데이터 타입
"""
class score:
    # 생성자 호출 시, 필드 초기화(__init__)
    def __init__(self, kor, eng, math):
        # 필드
        self.kor = kor
        self.eng = eng
        self.math = math

    # 메소드
    # 총점
    def calc_total(self):
        return self.kor + self.eng + self.math
    # 평균
    def calc_avg(self):
        return self.calc_total() / 3


# 클래스 객체(인스턴스)를 변수에 저장하고, 생성자 호출해 객체 생성
score1 = score(99, 88, 77)
# 객체(인스턴스) = score1

# 클래스 안의 메소드 호출 ~~~~~> 객체이름.메소드이름
print(score1.calc_total()) # 264
print(score1.calc_avg()) # 88.0

# 인스턴스 변경도 가능하다.
score1.math = 79
score1.eng = 100
print(score1.calc_total()) # 278
print(score1.calc_avg()) # 92.66666

# 다른 객체(인스턴스) 생성 ~~~~~> 객체이름.메소드이름
score2 = score(90, 85, 70)
print(score2.calc_total()) # 245
print(score2.calc_avg()) # 81.66666

