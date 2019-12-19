"""
Python으로 HTML 문서 분석
    필요 패키지
        beautifulsoup4 (HTML 요소 분석 패키지)
        html5lib (HTML 문서를 분석 패키지)
        requests (http 요청 보내고, 서버로부터 응답을 받는 기능을 사용하는 패키지)
"""
from bs4 import BeautifulSoup

# 파일을 읽기 모드로 오픈
with open('web01.html', mode='r', encoding='utf-8') as f:
    # HTML 문서를 파라미터에 전달해서 BeautifulSoup 객체 생성
    soup = BeautifulSoup(f, 'html5lib')
    # print(soup)

    # HTML 요소들 중에서 'h1'요소를 찾음
    h1 = soup.find('h1')
    print(h1) # <h1>처음 작성하는 HTML</h1>
    print(h1.text) # 처음 작성하는 HTML

    h2 = soup.h2 # 이렇게 해도 find() 함수를 쓴 결과와 같다
    print(h2) # <h2>HTML: HyperText Markup Language</h2>
    print(h2.text) # HTML: HyperText Markup Language

    # paragraph 요소 안의 문자열을 찾아 출력
    p = soup.p
    print(p) # <p>여기는 <b>paragraph</b>입니다.</p>
    print(p.text) # 여기는 paragraph입니다.

    # find()는 HTML 문서를 처음부터 분석을 하다가 가장 처음에 만나는 요소 1개만 리턴함
    print(soup.find('a'))
    print(soup.find_all('a')) # 그래서 여러개를 찾아서 리턴 하고자한다면 find_all() 사용

    print(soup('a')) # soup('태그이름')은 soup.find_all('태그이름')과 동일.

    # HTML 문서의 모든 링크에서 링크 주소(href)만 추출해 출력
    for link in soup('a'):
        # HTML 요소.get('attr이름') ~> attr의 값을 구함
        print(link.get('href'))

    








