"""
Class 작성 연습
"""
class Point:
    """
    2차원 평면 상의 점 1개를 저장하는 클래스
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        """
        Point 객체가 가지고 있는 점의 좌표를 출력
        :return: None
        """
        print(f'점의 좌표는 {self.x, self.y}입니다.')

    def distance(self, other):
        """
        두 점 사이의 거리를 리턴
        :param: 다른 Point 객체
        :return: 두 점 사이의 거리
        """
        import numpy as np
        return np.sqrt(((self.x - other.x)**2) + ((self.y - other.y)**2))

p1 = Point(3, 4)
p1.print_point()

p2 = Point(2, 1)
print(p2.distance(p1))

# --------------------------------------------------------------------------------

class ExTv:
    """
    ExTv Class(채널버튼, 음량버튼, 전원버튼)
    """
    def __init__(self, power, channel, volume):
        print('ExTv 생성자 호출')
        self.power = power
        self.channel = channel
        self.volume = volume

    # 전원 상태 메소드
    def PowerOnOff(self):
        if self.power: # power이 True면(켜져있으면)
            self.power = False
            print('TV Off')
        else: # 꺼져있으면
            self.power = True
            print('TV On')

    # 채널 변경 메소드
    def channelUp(self):
        if self.power is True:
            self.channel += 1

            if self.channel > 5:
               self.channel = 1
        else:
            pass
        print('Ch = ', self.channel)

    def channelDown(self):
        if self.power is True:
            self.channel -= 1

            if self.channel < 1:
               self.channel = 5
        else:
            pass
        print('Ch = ', self.channel)
    # 볼륨 변경 메소드
    def volumeUp(self):
        if self.power is True:
            if self.volume == 10:
                print('최대 볼륨입니다')
            else:
                self.volume += 1
                print('Vol = ', self.volume)
        else:
            pass
    def volumeDown(self):
        if self.power is True:
            if self.volume == 0:
                print('최소 볼륨입니다')
            else:
                self.volume -= 1
                print('Vol = ', self.volume)
        else:
            pass

# 클래스 정의(설계)

tv_ex = ExTv(True, 0, 0)
print(tv_ex.PowerOnOff())
tv_ex.PowerOnOff()
tv_ex.PowerOnOff()
tv_ex.PowerOnOff()
tv_ex.PowerOnOff()
tv_ex.PowerOnOff()


tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
tv_ex.volumeUp()
print('====================================')
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()
tv_ex.volumeDown()