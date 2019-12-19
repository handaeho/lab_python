"""
module06.py
"""
from numpy import random
print(random.randint(1, 100))
# numpy의 random을 import 했기 때문에, 맨 앞에 numpy를 붙이면 안됨.

import numpy
print(numpy.random.randint(1, 100))
# numpy만 import 했기 때문에, 맨 앞에 numpy를 반드시 붙여주어야 함.

# 위 두개는 서로 같은 기능을 수행하지만,
# import 구문의 형태에 따라, 작성해 주어야 하는 구문이 조금씩 다르다.

