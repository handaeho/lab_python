"""
module05.py
"""
from utils import *
# 'from 패키지 import *' 에서 import되는 모듈 이름들은
# 패키지 폴더의 '__init__.py' 파일의 '__all__' 변수에 설정된 모듈 이름들이다.
print(mymath01.pi)
# print(mymath02.mult(11, 12)) ~~~> '__all__'에 이 모듈은 없기 때문에 오류 발생.
# 'utils.__init__'의 '__all__'에서 다른 모듈에게 공개하기로 설정한 한 개의 모듈을 확인 가능.

import utils
print(utils.mymath02.mult(20, 30))
# 'utils.__init__.py'에서 'from . import mymath02'로 설정 했기 때문에 이 처럼 사용 가능.
# 'mymath01'은 사용 할 수 없다.

