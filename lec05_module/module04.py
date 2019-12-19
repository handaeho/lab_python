"""
module04.py

utils 패키지 안의 mymath01, mymath02 모듈을 사용하고자 한다.
"""
# from 패키지 import 모듈
from utils import mymath01
from utils import mymath02

print(mymath01.pi)
print(mymath02.div(10, 20))
