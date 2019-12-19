"""
icrawler 패키지를 사용해 google 이미지 검색 결과의 이미지 크롤링
"""
import os
from icrawler.builtin import GoogleImageCrawler

# 이미지 저장 경로
save_dir = os.path.join('C:' + os.sep, 'dev', 'images')

# GoogleImageCrawler 객체 생성, 스레드 설정 및 저장 공간 설정
google_crawler = GoogleImageCrawler(feeder_threads=1,
                                    parser_threads=1,
                                    downloader_threads=4,
                                    storage={'root_dir': save_dir})

# 검색 필터링(검색 조건)
filters = {'size': 'large', 'license': 'noncommercial,modify'}

# 저장 경로 폴더에 '슈퍼마리오' 이미지 다운로드
google_crawler.crawl(keyword='super mario', max_num=50)



