# <순서> open -> read -> close

# open
f = open('text.txt', mode='r', encoding='utf-8')

# read : read() 전체를 읽는다 / readline() 한 줄씩 읽는다
content = f.read(3) # read(n) ~~~> n개의 문자만 읽음
print(content)

content_line = f.readline()
print(content_line)

# close
f.close()

# -----------------------------------------------------------------

f = open('test2.txt', mode='r', encoding='utf-8')

line = f.readline() # 줄바꿈 문자(\n)까지 1줄로 읽어옴 (문서가 5줄이면 출력은 6줄이 되어버림)
print(f'line: {line}, length: {len(line)}')

line = f.readline()
line = line.strip() # strip() ~~~> 문자열 앞 뒤의 공백을 제거함
print(f'line: {line}, length: {len(line)}')

f.close()

# -----------------------------------------------------------------

# 무한 루프와 readline()을 사용해 문서 끝까지 읽기
f = open('test2.txt', mode='r', encoding='utf-8')

while True: # 무한 루프 시작
    line = f.readline()
    if line == '': # 파일의 끝(EOF, end Of File)은 비어있는 문자열이므로
        break # 무한 루프 종료
    print(line.strip())
    # Hello, World!
    # 안녕하세요, 세상!
    # 0123456789
f.close()

f = open('text.txt', mode='r', encoding='utf-8')

line = f.readline()

while line:
    print(line.strip())
    line = f.readline()

f.close()

with open('test2.txt', mode='r', encoding='utf-8') as f:
    # with 구문은 close 메소드를 자동으로 호출한다.
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
        # Hello, World!
        # 안녕하세요, 세상!
        # 0123456789

# -----------------------------------------------------------------

