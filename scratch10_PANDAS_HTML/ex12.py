"""
EX) 'http://www.hani.co.kr'에서 '특정 검색 결과 50개'의 'URL 주소', '기사 제목', '등록 시간', '내용'을 출력하고 텍스트 파일로 저장
"""
import requests
from bs4 import BeautifulSoup


def hani_search(keyword):
    url = 'http://search.hani.co.kr/Search?command=query&media=news&sort=d&period=all'
    # 검색 결과는 1 페이지 ~ 5 페이지 (pageseq=0 ~ pageseq=5)
    for page in range(5):
        print(f'============================ Page {page} ============================')
        # '검색어(keyword)'와 '페이지번호(pageseq)'를 'url'의 쿼리 스트링에 파라미터로 추가
        req_params = {'keyword': keyword, 'pageseq': page}
        response = requests.get(url, params=req_params) # 서버로 요청(request)을 보내고 응답(response)을 받음
        html = response.text.strip() # 서버로부터 받은 응답에서 html 문서 추출
        soup = BeautifulSoup(html, 'html5lib') # html 문서를 분석하기 위해 BeautifulSoup 객체 생성(parser는 html5lib)
        results = soup.select('ul.search-result-list li dt a') # 'a' 태그 경로 찾음

        for link in results:
            news_url = link.get('href') # 'a' 태그 경로 밑에 있는 'href' 태그(뉴스 기사 URL) 가져옴
            news_title = link.text.strip() # 기사 제목을 text 형식으로 가져옴

            article = hani_article(news_url) # 검색 결과 뉴스 URL을 하나씩 새로 열고 본문을 가져오기 위해 article 함수 호출

            write_file(news_url, news_title, article) # 결과들을 txt 파일로 저장하기 위해 write_file 함수 호출


def hani_article(url):
    """ url을 받아 기사를 한 개씩 열고 본문을 리턴하는 함수 """
    response =requests.get(url)
    html = response.text.strip()
    soup = BeautifulSoup(html, 'html5lib')
    article = soup.select('div.article-text div.text')[0].text.strip()
    # 'div.article-text div.text' 경로에서 가져온 결과는 '이 경로 밑의 모든 내용'을 '리스트의 형태'로 가져오기 때문에,
    # '리스트의 0번지 값'에 해당하는 값만이 '우리가 원하는 결과(해당 기사에 맞는 본문)'이므로 그 결과만을 text 형식으로 읽어온다.
    return article


def write_file(news_url, news_title, article):
    """ 크롤링 결과를 txt 파일로 저장하기 위한 함수 """
    hani = " "
    hani = hani + news_url +'\n' + news_title +'\n' + article # 전달받은 파라미터 값들을 text 형식으로 이어 붙임.
    with open('hani.txt', mode='a', encoding='utf-8') as f: # mode='a' : 쓰기모드. 파일이 있으면 뒤에 내용 추가
        f.writelines(hani)
    print(hani)


if __name__ == '__main__':
    hani_search('머신러닝')


