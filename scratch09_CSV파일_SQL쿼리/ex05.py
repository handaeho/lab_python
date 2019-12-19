"""
pandas를 사용한 gapminder.tsv 파일 활용
(tsv 파일 = 문자들이 'tab'으로 구분된 파일)

1) gapminder.tsv 파일을 데이터 프레임으로 변환
2) 데이터 프레임의 행/열 개수 확인
3) 데이터 프레임의 앞쪽 5행 확인
4) 데이터 프레임의 뒤쪽 5행 확인
5) 데이터 프레임의 각 컬럼들의 이름 출력
6) 데이터 프레임의 각 컬럼들의 타입 출력
7) 데이터 프레임에서 'country', 'lifeExp', 'gdpPercap' 컬럼들만 출력
8) 데이터 프레임에서 행 인덱스가 0, 99, 999인 행 출력
9) 데이터 프레임에서 행의 레이블이 840 ~ 851인 행들의 'country', 'lifeExp', 'gdpPercap'를 출력
10) 데이터 프레임에서 연도(year)별 기대수명의 평균 출력
11) 데이터 프레임에서 연도(year)별, 대륙(continent)별 기대수명의 평균 출력
"""
import pandas as pd
import matplotlib.pyplot as plt

# 1)
print(' 1번 ================================================================================== ')
gapminder = pd.read_csv('gapminder.tsv', sep='\t')
print(gapminder)

# 2)
print(' \n 2번 ================================================================================== ')
# dataframe.shape : (행 개수, 열 개수)
print('shape : ', gapminder.shape)

# 3), 4)
print(' \n 3번, 4번 ================================================================================== ')
# dataframe.head(n) : 처음 n개의 row를 출력. default는 5
# dataframe.tail(n) : 마지막 n개의 row를 출력. default는 5
print(gapminder.head())

print('--------------------------------------------')

print(gapminder.tail())

print('--------------------------------------------')

# dataframe.columns : pandas.Index 클래스 객체.  각 컬럼들의 이름으로 이루어진 리스트 출력
print(gapminder.columns)

# dataframe.iloc[row index, col index] ---> col index 생략하면 선택한 row index의 모든 col을 보여줌
# dataframe.loc[row label, col label] ---> label이 설정 되어있지 않으면, index가 자동으로 label이 됨
print(gapminder.iloc[0:5])
nrows, ncols = gapminder.shape
print(gapminder.iloc[nrows-5 : nrows]) # a : b ~> a <= x < b
print(gapminder.loc[0:10]) # gapminder 데이터 프레임엣는 따로 행 label이 없어, index가 label이 된다.

# 5), 6)
print(' \n 5번, 6번 ================================================================================== ')
# dataframe.dtypes : 각 컬럼(변수)의 타입.
# pandas 데이터 타입 : object(문자열), int64(64비트 정수), 64float(64비트 실수)
print(gapminder.dtypes)

print('--------------------------------------------')

# dataframe.describe() : 숫자형 변수들의 기술 요약 통계량
print(gapminder.describe())

# 7)
print(' \n 7번 ================================================================================== ')
# dataframe['컬럼이름', ...] : 컬럼이름에 해당하는 row 출력
cols = ['country', 'lifeExp', 'gdpPercap']
print(gapminder[cols])

# 8)
print(' \n 8번 ================================================================================== ')
print(gapminder.iloc[[0, 99, 999], [0, 3, 5]])

# 9)
print(' \n 9번 ================================================================================== ')
# dataframe.loc[row label, ['컬럼이름', ...]]
# dataframe.iloc[row index, [col index, ...]]
print(gapminder.loc[840:851, ['country', 'lifeExp', 'gdpPercap']])
print(gapminder.iloc[840:852, [0, 3, 5]])
# df.loc[a:b] ~~> a부터 b까지 출력. (label로 출력하므로)
# df.iloc[a:b] ~~> a부터 b-1까지 출력 (index로 출력하므로)

# 10)
print(' \n 10번 ================================================================================== ')
# dataframe.groupby('컬럼이름')
# ~~> 해당 ('컬럼이름')으로 그룹화된 리스트 (모든 컬럼이)
print(gapminder.groupby('year'))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001C1F3DF52C8>
# ~~~> 'DataFrameGroupBy object(객체)'

# dataframe.groupby('컬럼이름')['컬럼이름']
# ~~> 해당 ('컬럼이름')으로 그룹화된 결과 중, ['컬럼이름']에 해당하는 값을 가진 리스트
print(gapminder.groupby('year')['lifeExp'])
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x000001C7820A1948>
# ~~~> 'SeriesGroupBy object(객체)'

# SELECT avg(lifeExp) FROM gapminder GROUP BY year
print(gapminder.groupby('year')['lifeExp'].mean())

# 11번
print(' \n 11번 ================================================================================== ')
# SELECT avg(lifeExp) FROM gapminder GROUP BY year, continent
print(gapminder.groupby(['year', 'continent'])['lifeExp'].mean())

# CF 1)
print(' \n CF 1) 연도별 기대 수명 그래프 =========================================================== ')
# SELECT avg(lifeExp) FROM gapminder GROUP BY year
year_lifeExp = gapminder.groupby('year')['lifeExp'].mean()
print(year_lifeExp)

plt.plot(year_lifeExp)
plt.title('Life Exp by Year')
plt.show()

# CF 2)
print(' \n CF 2) 연도별 전 세계 인구 수 그래프 =========================================================== ')
# SELECT sum(pop) FROM gapminder GROUP BY year
year_pop = gapminder.groupby('year')['pop'].sum()
print(year_pop)

plt.plot(year_pop)
plt.title('Pop by Year')
plt.show()

