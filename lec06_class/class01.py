"""
Class : 프로그램에서 만들고자 하는 대상(객체)이 가져야 할 속성(데이터)과 가능(함수)들을 묶은 데이터 타입.

Method(메소드) ~> 클래스가 가지고 있는 함수(첫번째 파라미터로 self를 가짐(값을 전달하지는 않음))
Field(필드) ~> 클래스가 가지고 있는 데이터(변수)
"""
class BasicTv:
    """
    BasicTv Class(채널버튼, 음량버튼, 전원버튼)
    """
    # 생성자 호출 시, 필드 초기화(__init__)
    def __init__(self, power, channel, volume):
        print('BasicTv 생성자 호출')
        # 클래스가 가진 변수 ~~~> Field
        self.power = power
        self.channel = channel
        self.volume = volume

    # 클래스 내부에서 정의하는 함수 ~~~> Method
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
        self.channel += 1
        print('Ch = ', self.channel)
    def channelDown(self):
        self.channel -= 1
        print('Ch = ', self.channel)

    # 볼륨 변경 메소드
    def volumeUp(self):
        self.volume += 1
        print('Vol = ', self.volume)
    def volumeDown(self):
        self.volume -= 1
        print('Vol = ', self.volume)

# 클래스 정의(설계)


# 클래스 객체(인스턴스)를 생성해, 변수에 저장(tv1)
# 생성자(BasicTv) 호출 ~~~~~> 객체 생성됨.
tv1 = BasicTv(power=False, channel=0, volume=0)

print(tv1) # <__main__.BasicTv object at 0x000001DB067D2A48>
print(tv1.power)# False
print(tv1.channel) # 0
print(tv1.volume) # 0

# 작성한 PowerOnOff 메소드 이용.
# tv1이 self가 되는 것(self의 주소를 가짐). self를 직접 써주지는 않는다.

# 전원 상태
tv1.PowerOnOff() # TV On ~~~> 켜짐
tv1.PowerOnOff() # TV Off ~~~> 다시 꺼짐

# 채널 변경
tv1.channelUp() # Ch =  1
tv1.channelUp() # Ch =  2
tv1.channelDown() # Ch =  1
tv1.channelDown() # Ch =  0

# 볼륨 변경
tv1.volumeUp() # Vol = 1
tv1.volumeUp() # Vol = 2
tv1.volumeDown() # Vol = 1
tv1.volumeDown() # Vol = 0

# tv2 생성자 호출
tv2 = BasicTv(power=True, channel=100, volume=5)

# tv2의 전원 상태
tv2.PowerOnOff()
tv2.PowerOnOff()

# tv2의 채널 변경
tv2.channelUp()
tv2.channelUp()
tv2.channelDown()
tv2.channelDown()

# tv2의 볼륨 변경
tv2.volumeUp()
tv2.volumeUp()
tv2.volumeDown()
tv2.volumeDown()
