import numpy as np
import pandas as pd

def fill_group_mean(df):
    group_mean = df['data'].mean()
    print(group_mean)

    return df.fillna(group_mean)


if __name__ == '__main__':
    # Series 생성
    np.random.seed(1234)
    s = pd.Series(np.random.randint(1, 10, 5))
    print(s)

    s[3] = np.nan # 원소 1개를 NA로 변경
    print(s)

    # NA를 평균값으로 대체하기 위해 평균을 먼저 계산
    m = s.mean() # numpy, pandas의 집계 함수들은 NA를 제거하고 계산됨.
    print(m)

    # NA를 계산한 평균 m으로 대체
    s = s.fillna(m)
    print(s)

    df = pd.DataFrame({
        'province': ['서울', '경기', '충청', '전라', '강원', '경상', '부산'],
        'division': ['west'] * 4 + ['east'] * 3,
        'data': np.random.randint(1, 10, 7)
    })
    print(df)

    # 데이터 2개를 NA로 대체
    df.iloc[0, 2] = np.nan
    df.iloc[6, 2] = np.nan
    print(df)

    # 우리가 만든 fill_group_mean() 함수를 사용해 df의 NA를 각 그룹의 평균값으로 대체
    grouped = df.groupby('division') # DataFrameGroupBy 객체
    cleaned = grouped.apply(fill_group_mean)
    # GroupBy.apply(fn)는 함수 fn의 첫번째 파라미터 df에 DataFrameGroupBy 객체를 전달
    print(cleaned)



