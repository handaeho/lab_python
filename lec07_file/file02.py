"""
<순서>
1) 파일 open
2) 파일 read / write
3) 파일 close

꼭 지켜야 한다!
"""
# 파일 열기 open('파일이름', 'mode', ...)
f = open('text.txt', 'w', encoding='utf-8') # 'w' 쓰기 모드

# 파일에 텍스트 쓰기
for i in range(1, 11):
    f.write(f'{i}번째 줄... \n')

# 파일 닫기 close()
f.close()

# with 구문 : 리소스를 사용한 후, close() 메소드를 자동으로 호출
# with ~ as 변수:
#    실행문
with open('test2.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World! \n')
    f.write('안녕하세요, 세상! \n')
    f.write('0123456789 \n')

