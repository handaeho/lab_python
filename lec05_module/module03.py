"""
module03.py
"""
#'utils' 패키지(디렉토리)의 'mymath01' 모듈(파이썬 파일)의 변수, 함수들을 사용 해보자.
# 1) import 모듈이름
# 2) from 모듈이름 import 변수, 함수 등
# 3) from 패키지 import 모듈이름

# import utils.mymath01 ~~~> 이렇게 import하면,
# print('pi = ',utils.mymath01) ~~~> 이렇게 작성해야 한다.

from utils.mymath01 import pi
print('pi = ', pi) # 3.14 ~~~> utils.mymath01의 pi를 그대로 사용 할 수 있다.
