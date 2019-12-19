"""
os 모듈의 변수 & 함수
"""
import os

# CWD : Current working directory(현재 작업 디렉토리 / 폴더)
print(os.getcwd()) # C:\dev\lab-python\lec07_file

# -------------------------------------------------------------------------------------------
# 절대 경로(Absolute Path) = 시스템의 root부터 현재 위치까지 전체 경로를 표시하는 방법
# C:\dev\lab-python\lec07_file ~~~> Windows
# /Users/user/Documents ~~~> Linux

# 상대 경로(Relative Path) = 혀재 작업 디렉토리를 기준으로 경로를 표시하는 방법
# . (현재 디렉토리) / .. (상위 디렉토리(한 단계 위))
# ..\lec06_class\inheritance01.py ~~~절대 경로로 바꾸면~~~> C:\dev\lab-python\lec07_class\inheritance01.py
# -------------------------------------------------------------------------------------------

# OS 종류 확인
print(os.name) # nt

# temp.txt 파일 생성
if os.name == 'nt': # Windows OS면
    file_path = '.\\temp\\temp.txt' # 반드시 경로에는 '\\(백 슬래쉬)' 두 개를 사용할 것
else: # Windows OS가 아니면
    file_path = './temp/temp.txt' # '/(슬래쉬)'는 하나만 써도 됨

print(file_path) # .\temp\temp.txt

# 하지만 매번 이렇게 하는 것은 너무 귀찮다! ~~~> os.path.join('경로', '텍스트 이름')
# 파일 구분자를 해당 OS에 맞게끔 경로 설정 해준다.
file_path = os.path.join('.', 'temp', 'temp.txt')
print(file_path) # .\temp\temp.txt

print(os.path.isdir('.')) # True ~~~> 현재 위치(.)가 디렉토리냐? True
print(os.path.isdir('file01.py')) # False ~~~> 이 위치(file01.py)가 디렉토리냐? False

print(os.path.isfile('.')) # False ~~~> 현재 위치(.)가 파일이냐? False
print(os.path.isfile('file01.py')) # True ~~~> 이 위치(file01.py)가 파일이냐? True

# 넓은 의미의 파일(file) ~~~> 디렉토리(dir) & 파일(file)
# 좁은 의미의 파일(file) ~~~> dox, txt, ppt, ...

# 현재 디렉토리 스캔 후, 내용 보기
with os.scandir('.') as my_dir: # 현재 디렉토리(.)를 스캔하고 내용을 'my_dir'이라는 변수로 저장하겠다.
    # my_dir은 리스트가 된다.
    for entry in my_dir:
        print(entry.name, '\t', entry.is_file())
        # file01.py     True
        # temp      False
        # __init__.py      True

# 파일, 디렉토리 이름 변경 ~~~> os.rename('예전 이름', '바꿀 이름')
try:
    os.rename('temp', 'test')
except FileNotFoundError:
    print('해당 이름의 폴더가 존재하지 않습니다.')

# 파일 삭제 ~~~> os.remove('삭제할 파일')
# 디렉토리 삭제 ~~~> os.rmdir('삭제할 디렉토리')
try:
    os.rmdir('test')
    print('디렉토리 삭제 완료')
except FileNotFoundError:
    print('권한이 없습니다.')

# 파일, 디렉토리 생성 ~~~> os.mkdir('생성할 폴더 또는 디렉토리 이름')
try:
    os.mkdir('test2')
except FileExistsError:
    print('이미 존재하는 파일 또는 디렉토리입니다.')

# os.makedirs(path, mode, exist_ok)
# ~~~> 중간 단계 디렉토리가 없어도 디렉토리를 새롭게 생성하고 동시에 하위에 파일 또는 디렉토리 생성
try:
    os.makedirs('test1\\temp')
except FileExistsError:
    print('이미 존재하는 파일 또는 디렉토리입니다.')

