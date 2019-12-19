import requests
from bs4 import BeautifulSoup

# 접속할 주소
url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=2'

# 사이트(웹 서버)에 request 전송
html = requests.get(url).text.strip() # request의 결과를 html 변수에 저장

# HTML 문서의 모든 링크에 걸려있는 주소 출력
soup = BeautifulSoup(html, 'html5lib') # soup 객체 생성, parser는 'html5lib'
for link in soup.find_all('a'): # soup 객체에서 'a' 태그 목록을 모두 찾음
    print(link.text.strip(), link.get('href')) # 'a' 태그 목록 중, 'href'(링크) 속성 값 가져옴 (공백 제거한 제목까지)

print(' ============================================================================== ')

# 뉴스 링크만 찾기
div_coll_cont = soup.find_all(class_='coll_cont') # 'class'가 'coll_cont'인 요소를 모두 찾음
# 위는 soup.find_all(attrs={'class': 'coll_cont'})와 같음.
print(len(div_coll_cont)) # class가 coll_cont는 모두 4개

# 같은 클래스 이름을 갖는 요소가 여러개이므로 원하는 요소를 찾아야 한다.
# HTML 하위요소(sub/child element)를 찾는 방법
# 1) parent_selector > child_selector
#   태그이름 > 태그이름 (ex)'div > ul > li')
#   --> 태그 이름 뿐만 아닌,클래스 이름도 사용 가능하다. (.클래스이름 > .클래스이름)
#       (ex) .coll_cont > #clusterResultUL > .fst) ---> '#'은 '아이디 속성'을 의미(id=clusterResultUL)
# 2) ancestor_selector descendant_selector
#    조상 선택자 자손 선택자 (ex) div li)
#    ---> 클래스 이름으로 사용할 수도 있다. (.클래스이름 .클래스이름)
#        (ex) .coll_cont .fst) --> '.coll_cont' 클래스의 자식 요소들 중, 클래스가 '.fst'인 요소들
# '>' 를 쓰는 방식은 경로를 처음부터 전부 다 지정해 주는 것이다. / ' '를 쓰는 방식은 중간에 경로를 건너 뛰어도 된다.

# soup.select(css_selector) -> soup 객체에서 CSS 선택자로 요소들을 찾기
news_link = soup.select('.coll_cont ul li a.f_link_b')
# 'coll_cont 클래스' 밑에 'ul 태그'를 찾고, 또 그 밑의 'li 태그'를 찾고, 다시 그 밑의 'a 태그' 중, 'a.f_link_b'를 찾아라.
for link in news_link:
    print(link.get('href')) # 그렇게 찾은 것('a.f_link_b' 태그)들 중, '링크 부분'에 해당하는 'href' 태그만을 가져온다.
# https://cp.news.search.daum.net/p/87257246
# http://v.media.daum.net/v/20191206104223990?f=o
# http://v.media.daum.net/v/20191206081549155?f=o
# http://v.media.daum.net/v/20191128200443076?f=o
# https://cp.news.search.daum.net/p/87157229
# https://cp.news.search.daum.net/p/87103956
# https://cp.news.search.daum.net/p/87068633
# https://cp.news.search.daum.net/p/87212496
# http://v.media.daum.net/v/20191123120109125?f=o
# http://v.media.daum.net/v/20191113202402907?f=o
# ~~~> 이렇게 'href 태그'를 갖는 모든 링크 중, 뉴스 링크만 가져올 수 있다.



