"""
1) csv 파일(stock_price.csv) write
    6/20/2019, AAPL, 90.91
    6/20/2019, MSFT, 41.68
    6/21/2019, AAPL, 90.86
    6/21/2019, MSFT, 41.51

2) csv 파일을 csv.reader를 사용해 파일의 내용을 리스트로 변환하고 각 종목의 가격 평균을 계산 후, 출력

3) csv 파일을 csv.Dictreader를 사용해 파일의 내용을 dict 리스트로 변환하고 각 종목의 가격 평균을 계산 후, 출력
"""
import csv

# 1) csv 파일(stock_price.csv) write
row1 = ['6/20/2019', 'AAPL', 90.91] # 문자열 리스트
row2 = ['6/20/2019', 'MSFT', 41.68]
row3 = ['6/21/2019', 'AAPL', 90.86]
row4 = ['6/21/2019', 'MSFT', 41.51]
result = [row1, row2, row3, row4]

with open('stock_price.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=',') # csv writer 객체 생성
    for row in result: # writer 객체의 writerow() 메소드를 사용해 한 줄씩 쓰기
        writer.writerow(row)

# 2) csv 파일을 csv.reader를 사용해 파일의 내용을 리스트로 변환하고 각 종목의 가격 평균을 계산 후, 출력
with open('stock_price.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    df = [line for line in reader]
print(df)
# [['6/20/2019', 'AAPL', '90.91'], ['6/20/2019', 'MSFT', '41.68'], ['6/21/2019', 'AAPL', '90.86'], ...

AAPL_Prices = [float(item[2]) for item in df if item[1] == 'AAPL']
# ~> item의 1번지 값이 'AAPL'이면, 2번지 값을 리스트에 추가
MSFT_Prices = [float(item[2]) for item in df if item[1] == 'MSFT']
# ~> item의 1번지 값이 'MSFT'이면, 2번지 값을 리스트에 추가
print(AAPL_Prices, MSFT_Prices) # [90.91, 90.86] [41.68, 41.51]

AAPL_avg = sum(AAPL_Prices) / len(AAPL_Prices)
MSFT_avg = sum(MSFT_Prices) / len(MSFT_Prices)
print(f'AAPL의 평균 가격: {AAPL_avg} / MSFT의 평균 가격 : {MSFT_avg}')
# AAPL의 평균 가격: 90.88499999999999 / MSFT의 평균 가격 : 41.595

# 3) csv 파일을 csv.Dictreader를 사용해 파일의 내용을 dict 리스트로 변환하고 각 종목의 가격 평균을 계산 후, 출력
with open('stock_price.csv', mode='r', encoding='utf-8') as f:
    col_name = ['date', 'stock', 'price']
    reader = csv.DictReader(f, fieldnames=col_name)
    # 'stock_price.csv'에는 컬럼 이름이 없으므로 'fieldnames' 파라미터에 '컬럼 이름으로 줄 값'을 전달한다.
    df = [row for row in reader]
print(df)
# [OrderedDict([('date', '6/20/2019'), ('stock', 'AAPL'), ('price', '90.91')]), ...

AAPL_Prices = [float(item['price']) for item in df if item['stock'] == 'AAPL']
# ~> item의 key가 'stock', value가 'AAPL'이면서 key가 'price'인 value를 리스트에 추가.
MSFT_Prices = [float(item['price']) for item in df if item['stock'] == 'MSFT']
# # ~> item의 key가 'stock', value가 'MSFT'이면서 key가 'price'인 value를 리스트에 추가.

AAPL_avg = sum(AAPL_Prices) / len(AAPL_Prices)
MSFT_avg = sum(MSFT_Prices) / len(MSFT_Prices)
print(f'AAPL의 평균 가격: {AAPL_avg} / MSFT의 평균 가격 : {MSFT_avg}')
# AAPL의 평균 가격: 90.88499999999999 / MSFT의 평균 가격 : 41.595