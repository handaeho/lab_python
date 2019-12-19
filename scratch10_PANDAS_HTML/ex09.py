from bs4 import BeautifulSoup

with open('web02.html', mode='r', encoding='utf-8') as f:
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(f, 'html5lib')

    # HTML 문서 안의 모든 div 태그 찾기
    for div in soup.find_all('div'): # soup.find_all('태그이름')과 soup('태그이름')은 동일한 기능
        print(div)
        print(div.text)
        # <div class="class1">여기는 class1 입니다. </div>
        # 여기는 class1 입니다.
        # <div class="class1">여기는 class1 입니다. </div>
        # 여기는 class1 입니다.
        # <div class="class2">여기는 class2 입니다. </div>
        # 여기는 class2 입니다.
        # <div class="class2" id="id1">여기는 class2 입니다. </div>
        # 여기는 class2 입니다.

    # HTML 문서의 'class1' 속성을 갖는 모든 요소 찾기
    for cls_1 in soup.find_all(attrs={'class': 'class1'}): # attrs = {'태그이름': '클래스이름'}
        print(cls_1)
        # <div class="class1">여기는 class1 입니다. </div>
        # <div class="class1">여기는 class1 입니다. </div>

    # # HTML 문서의 'class2' 속성을 갖는 모든 요소 찾기
    for cls_2 in soup(class_='class2'): # class_ = '클래스이름'
        print(cls_2)
    # 'class'는 변수 이름으로 사용할 수 없으므로 'class_' 라고 한다.

    # HTML 문서의 'id1' 아이디 속성을 갖는 요소 찾기
    for id_1 in soup(attrs={'id': 'id1'}):
        print(id_1)
        # <div class="class2" id="id1">여기는 class2 입니다. </div>
        # <div class="class2" id="id1">여기는 class2 입니다. </div>
    
