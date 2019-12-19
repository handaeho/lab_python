"""
for line in 파일:
    실행문

~~~> 파일에서 readline()을 호출한 결과를 line 변수에 저장.
line이 빈 문자열('')이 아닐때, 실행문 시작.
line이 빈 문자열('')이면, for 루프 종료.
"""
with open('text.txt', mode='r', encoding='utf-8') as f:
    for line in f: # f에서 readline()을 호출해 line에 전달.
        print(line.strip()) # 공백 열 제거 후, 출력
