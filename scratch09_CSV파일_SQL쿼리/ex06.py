import os

import pandas as pd

# gapminder.tsv 파일을 읽어 dataframe 생성
df = pd.read_csv('gapminder.tsv', sep='\t', encoding='utf-8')
print(df.iloc[0:5])

# 조건에 맞는 row를 출력해보자.
#  ~~~> Boolean Indexing : 컬럼의 값을 이용해서 특정 레코드(row)들을 선택.
# Dataframe[컬럼의 값을 이용한 조건식] ~> 조건식의 결과는 TRUE / FALUE
# SELECR * FROM dataframe WHERE column == ' '
df_afg = df[df['country'] == 'Afghanistan'] # df['country']의 값이 'Afghanistan'과 같은 레코드들을 선택
print(df_afg)

print('----------------------------------------------------------------------------------------')

df_kor = df[df['country'] == 'Korea, Rep.'] # # df['country']의 값이 'Korea, Rep.'과 같은 레코드들을 선택
print(df_kor)

print('----------------------------------------------------------------------------------------')

# 대한민국('Korea, Rep.')의 인구(pop)와 1인당 GDP(gdpPercap)을 출력
kor_pop_gdp = df_kor[['pop', 'gdpPercap']]
print(kor_pop_gdp)
# 또는
kor_pop_gdp = df[df['country'] == 'Korea, Rep.'][['pop', 'gdpPercap']] # df[조건식][['컬럼이름', ...]]
print(kor_pop_gdp)

print('----------------------------------------------------------------------------------------')

# mpg.csv 파일을 읽어 데이터 프레임 생성
file_path = os.path.join('..', 'scratch08_경사하강법', 'mpg.csv')
mpg = pd.read_csv(file_path, encoding='utf-8')

print(type(mpg)) # <class 'pandas.core.frame.DataFrame'>

print(type(mpg['cty'])) # <class 'pandas.core.series.Series'>
print(mpg['cty'])

print(type(mpg[['cty']])) # <class 'pandas.core.frame.DataFrame'> (= SELECT cty FROM mpg)
print(mpg[['cty']])
# ~~~> 'Series 타입'은 출력하면 바로 '컬럼 이름 없이 데이터'가 나오고,
# 'DataFrame 타입'은 출력하면 '컬럼 이름이 나오고, 데이터'가 나온다.

# cty 컬럼의 값이 cty의 평균보다 큰 차들의 model, cty, hwy를 출력
print(mpg['cty'].mean())
above_mean_cty_car = mpg[mpg['cty'] > mpg['cty'].mean()][['model', 'cty', 'hwy']]
print(above_mean_cty_car)

print('----------------------------------------------------------------------------------------')



