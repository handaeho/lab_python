"""
Inheritance(상속) : 부모 클래스에게서 필드와 메소드등을 물려받아 자식 클래스가 사용하는 것. 코드 재 사용성 Up.

- 부모 클래스 -> parent class, super class, base class
- 자식 클래스 -> child class, sub class, derive class

자식 클래스는 부모 클래스의 필드와 메소드들을 그대로 물려받아 사용하고, 확장까지도 가능하다.
"""
class Shape: # 부모 클래스
    def __init__(self, x=0, y=0):
        """
        초기화(__init__) 메소드 ~~~> 필드 지정.
        :param x: x 좌표
        :param y: y 좌표
        """
        print('Shape __init__ 호출')
        self.x = x
        self.y = y

    def __repr__(self):
        """
        representation 메소드 ~~~> 출력문을 만듦(문자열을 리턴).
        :return: 문자열
        """
        return f'Shape >>> x = {self.x}, y = {self.y}'

    def move(self, dx, dy):
        """
        x와 y가 이동할 거리
        :param dx: x가 이동할 거리
        :param dy: y가 이동할 거리
        :return:
        """
        self.x += dx
        self.y += dy

    def area(self): # 도형의 면적 계산
        """
        도형마다 넓이를 구하는 공식이 다르므로 Shape 객체는 넓이를 계산 할 수 없고,
        자식 클래스들인 Rectangle, Circle 객체들이 각자의 공식으로 계산해야 한다.

        :return: 도형의 넓이
        """
        raise NotImplementedError('반드시 Override가 필요합니다.')
        # Shape 객체에서는 넓이를 계산하지 않고 자식 클래스에서 override 해서 계산하기 때문에
        # 만약, override를 하지 않을 경우 에러 발생시킴.

    def draw(self):
        """
        도형의 넓이를 계산하는 area 메소드를 사용해서 도형 내부를 그려주는 메소드
        실제로 그래픽 작업은 아니고, 그 방식을 학습하기 위함.
        :return: None
        """
        print(f'Drawing Area {self.area()}...')
        # 자식 클래스에서 override 되어 리턴된 area 메소드가 draw 메소드에 전달되어 출력

# class 자식클래스이름(부모클래스이름):
#   클래스 body
class Rectangle(Shape): # Shape 클래스를 상속받는 자식 클래스인 사각형(Rectangle) 클래스
    # 자식 클래스 확장
    def __init__(self, w=0, h=0, x=0, y=0):
        """
        __init__ 메소드가 호출 되어야지만, self.x, self.y가 생성된다.
        자식 클래스에서 __init__ 메소드를 안 만들면, 부모 클래스의 __init__ 메소드가 자동으로 호출 되지만,
        자식 클래스에서 __init__ 메소드를 생성하면, 자동으로 호출되지 않는다.
        따라서, 자식 클래스에서 부모 클래스의 __init__ 메소드를 명시적으로 반드시 호출 필요.
        :param w: 자식 클래스만 가진 길이
        :param h: 자식 클래스만 가진 높이
        :param x: 부모 클래스에 있는 x 좌표
        :param y: 부모 클래스에 있는 y 좌표
        """
        super().__init__(x, y) # 슈퍼 클래스(부모 클래스)의 __init__ 메소드 호출

        # 부모 클래스의 필드(x, y) 이외에 자식 클래스가 확장되어 추가로 가질 높이(h)와 길이(w) 필드
        self.w = w
        self.h = h
        print('Rectangle.__init__ 호출')

    def __repr__(self): # 자식 클래스가 가질 출력문 메소드(문자열 리턴)
        """
        Override : 부모 클래스로부터 상속받은 메소드를 자식 클래스에서 새롭게 재 정의 하는 것.
        :return: 문자열
        """
        return f'사각형 <<가로 : {self.w}, 높이 : {self.h}, x = {self.x}, y = {self.y}>>'

    def area(self):
        """
        사각형 넓이 공식에 맞게 부모 클래스의 area 메소드를 Override.
        :return: 사각형의 넓이 = w * h
        """
        return self.w * self.h

class Circle(Shape): # Shape 클래스를 상속받는 자식 클래스인 원(Circle) 클래스
    def __init__(self, r=0, x=0, y=0):
        # 슈퍼 클래스(부모 클래스)의 __init__ 메소드 반드시 호출
        super().__init__(x, y)
        # 위는 Shape.__init__(self, x, y)과 같다. 이때는 'self'를 생략하지 못한다.
        # 이런 형태는 부모가 여럿이고, 자식은 하나인 '다중 상속 관계'에서 사용한다.
        # 부모가 A, B 둘이면, A.__init(self, x, y) / B.__init__(self, a, b)
        # 그런데 다중 상속 시, 부모 클래스들에 같은 이름의 메소드가 있으면 문제가 발생한다.
        # 파이썬은 오버로딩 기능이 없어, 둘 중 하나의 메소드가 덮어 씌워져 버린다.

        # 자식 클래스를 확장하여 부모 클래스의 필드(x, y)에 자식 클래스만의 필드(r)를 추가하고 초기화함.
        self.r = r
        print('Circle.__init__ 호출')

    def __repr__(self):
        return f'원 << 반지름 : {self.r}, x : {self.x}, y : {self.y}>>'

    def area(self): # 원 넓이 공식에 맞게 부모 클래스의 area 메소드를 Override.
        return 3.14 * (self.r ** 2)


if __name__ == '__main__':
    shape1 = Shape(0, 0)
    print(shape1)
    shape1.move(1, 2)
    print(shape1)
    # Shape __init__ 호출
    # Shape >>> x=0, y=0
    # Shape >>> x=1, y=2

    print('--------------------------------------')

    # 자식 클래스를 호출하면, 부모 클래스의 메소드들을 물려받아 그대로 사용한다.

    rect1 = Rectangle(w=3, h=4, x=0, y=0)
    print('type : ', type(rect1))
    print('rect1 : ', rect1) # override 한 __repr__메소드가 호출됨
    rect1.move(-1, -2) # 부모에게서 상속받은 move 메소드가 호출됨
    print(rect1)
    # Shape __init__ 호출
    # Rectangle.__init__ 호출
    # type :  <class '__main__.Rectangle'>
    # rect1 :  사각형 <<가로 : 3, 높이 : 4, x = 0, y = 0>>
    # 사각형 <<가로 : 3, 높이 : 4, x = -1, y = -2>>

    print('--------------------------------------')

    circle1 = Circle(r=5, x=0, y=0)
    print('type : ', type(circle1))
    print('circle1 : ', circle1)
    circle1.move(2, 2)
    print(circle1)
    # Shape __init__ 호출
    # Circle.__init__ 호출
    # type :  <class '__main__.Circle'>
    # circle1 :  원 << 반지름 : 5, x : 0, y : 0>>
    # 원 << 반지름 : 5, x : 2, y : 2>>

    print('--------------------------------------')

    rect1.draw() # Drawing Area 12..
    circle1.draw() # Drawing Area 78.5...



