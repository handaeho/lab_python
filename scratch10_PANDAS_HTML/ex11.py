"""
Q1) 'www.daum.net'에서 '머신러닝' 검색 기사 중, 기사 100개의 URL 주소와 제목 출력
Q2) 'www.daum.net'에서 임의의 검색어로 검색한 기사 100개의 URL 주소와 제목 출력

웹 주소(URI, URL)의 형식
~> 프로토콜://서버주소[:포트번호]/경로?쿼리스트링

https://www.naver.com
https://sports.news.naver.com/news.nhn?oid=003&aid=0009597324

쿼리 스트링(Query String) : 클라이언트(qmfkdnwj)가 서버로 보내는 정보.
    'param이름=param값' 형식으로 작성
    파라미터가 여러개일 경우, '&'로 파라미터들을 구분
"""
import requests
from bs4 import BeautifulSoup

def daum_search(keyword):
    url = 'https://search.daum.net/search?w=news&DA=YZR&spacing=0'
    # 검색 결과는 1 페이지 ~ 10 페이지
    for page in range(1, 11):
        print(f'============================ Page {page} ============================')
        req_params = {'q': keyword, 'p': page} # '검색어(keyword)'와 '페이지번호'를 'url'의 쿼리 스트링에 파라미터로 추가
        response = requests.get(url, params=req_params)
        html = response.text.strip()

        soup = BeautifulSoup(html, 'html5lib')
        news_links = soup.select('.coll_cont ul li a.f_link_b')
        for link in news_links:
            news_url = link.get('href')
            news_title = link.text.strip()
            print(news_title, news_url)


if __name__ == '__main__':
    # Q1)
    print(f'\n =============================================== Q1 ===============================================')

    for n1 in range(1, 11):
        url = f'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p={n1}'
        html = requests.get(url).text.strip()

        soup = BeautifulSoup(html, 'html5lib')

        news_link = soup.select('.coll_cont ul li a.f_link_b')

        print(f'\n ============================== 페이지 {n1} ==============================')
        for link in news_link:
            print(link.text.strip(), link.get('href'))

    # Q2)
    print(f'\n =============================================== Q2 ===============================================')

    x = input('\n 검색어 입력 = ')
    for n2 in range(1, 11):
        # q='검색어'&p='페이지번호'
        url = f'https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&cluster=y&q={x}&p={n2}'

        html = requests.get(url).text.strip()

        soup = BeautifulSoup(html, 'html.parser')

        news_link = soup.select('.coll_cont ul li a.f_link_b')

        print(f'\n ============================== 페이지 {n2} ==============================')
        for link in news_link:
            print(link.text.strip(), link.get('href'))

# Teacher Ver. ========================================================================================================

    # Q1
    print(f'\n ================================= Q1 Teacher Ver. ========================================')
    url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=0'
    for page in range(1, 11):
        print(f'============================ Page {page} ============================')
        # 해당 페이지 URL 주소로 get 방식 요청 보내고 서버에서 보낸 응답을 문자열 처리
        # requests.get(url, params={})
        # ~> 'params={}'의 내용을 'url'의 쿼리 스트링 파라미터로 추가해준다.
        # 즉, 'get'의 파라미터로 'url'과, 함께 보내고자 하는 쿼리문인 'p=page'를 dict 형태로 전달한다.(page = 페이지번호)
        html = requests.get(url, params={'p': page}).text.strip()

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html, 'html5lib')
        news_link = soup.select('.coll_cont ul li a.f_link_b')
        for link in news_link:
            print(link.text.strip(), link.get('href'))
            # HTML 요소의 'href' 속성 값과


    # Q2
    print(f'\n ================================= Q2 Teacher Ver. ========================================')
    daum_search('신서유기')

