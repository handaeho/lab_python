# from 모듈이름 import 변수 or 함수
from math import pi
print(pi) # 3.141592653589793~~~> 'math.pi'라고 하지 않는다.
# 또한, 'pi'만 가져왔기 때문에, sqrt / sum 등은 쓸 수 없다. 쓰고 싶으면 import 해야함.

# --------------------------------------------------------------------------
from math import * # math의 모든 기능(변수, 함수등)을 import 하겠다.

print(sin(pi / 2)) # 1.0
pi = 3.14
print(sin(pi / 2)) # 0.9999996829318346
# 이렇게 math에 있는 pi등의 이름을 변수로 써버리면, math에서 pi를 이용한 계산들이 모두 틀려진다.
# 따라서 'from ~ import *'은 좋은 설계가 아니다.

# --------------------------------------------------------------------------
# import ~ as 별명
import numpy as np
print(np.random.randint(0, 10))
