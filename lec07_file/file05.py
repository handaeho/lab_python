"""
<file open mode>
- r : read. 읽기 mode ~> 파일이 없으면 'FileNotFoundError' 발생
- w : write. 쓰기 mode ~> 파일이 없으면 새로운 파일을 생성. 에러 발생 X.
                         기존 파일이 있으면 열어줌. 단, 기존 파일 내용이 날아감.(덮어씌워짐)
- a : append. 추가 mode ~> 파일이 없으면 새로운 파일을 생성. 에러 발생 X.
                          기존 파일이 있으면, 맨뒤에 파일 포인터가 위치함. 새로운 내용은 파일 끝에 추가됨.
"""
# r
try:
    with open('NoFile.txt', mode='r') as f:
        pass
except FileNotFoundError:
    pass

# w
with open('NewFile.txt', mode='w', encoding='utf-8') as f:
    f.write('test 테스트...')

with open('NewFile.txt', mode='w', encoding='utf-8') as f:
    pass # pass를 하더라도, NewFile의 내용이 전부 사라짐

# a
with open('Append.txt', mode='a', encoding='utf-8') as f:
    f.write('test 123 \n')

