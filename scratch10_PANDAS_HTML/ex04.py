"""
tips.csv 파일
"""
import pandas as pd

from scratch10_PANDAS_HTML.ex02 import peak_to_peak

if __name__ == '__main__':
    # tips.csv 파일을 읽어 데이터 프레임 생성
    tips = pd.read_csv('tips.csv')

    # 앞 5개 데이터 출력
    print(tips[0:5])
    print('\n ============================================================')

    # DataFrame에 'tip_pct' 컬럼 추가 (tip_pct = 팁 금액 / 총 금액)
    tip_pct = tips['tip'] / tips['total_bill']
    tips['tip_pct'] = tip_pct

    print(tips[0:5])
    print('\n ============================================================')

    # day, smoker 별 그룹을 지어 tip_pct 평균 출력
    grouped = tips.groupby(['day', 'smoker'])
    day_smoker_tip_pct = grouped['tip_pct']
    result_mean = day_smoker_tip_pct.agg('mean')

    print(result_mean.unstack())
    print('\n ============================================================')

    # day 별, smpker 별 그룹의 tip_pct 평균, 표준편차, 최대/최소 차이 출력
    print(day_smoker_tip_pct.agg(['mean', 'std', peak_to_peak]))

    # day 별, smpker 별 그룹의 tip_pct, total_bill 평균, 표준편차, 최대/최소 차이 출력
    grouped_pct_bill = grouped[['tip_pct', 'total_bill']]
    print(grouped_pct_bill.agg([('average', 'mean'),
                                ('std-dev', 'std'),
                                ('range', peak_to_peak)]))

    # groupby 객체의 컬럼들마다 다른 함수를 agg()로 적용할 때
    # ~~~> agg({'col_name': [functions], ...})
    # 그룹화된 데이터프레임에서 'tip' 컬럼에는 'max' 함수를, 'size' 컬럼에는 'sum' 함수를 aggregate
    result = grouped.agg({'tip': 'max', 'size': 'sum'})
    print(result)

    functions = ['mean', 'std', peak_to_peak]
    result = grouped.agg({
        'tip_pct': functions,
        'total_bill': functions
    })
    print(result)
    # 이렇게 컬럼 이름과 함수들의 튜플로 적용 할 수 있다.
    functions_2 = [('mu', 'mean'), ('sigma', 'std'), ('range', peak_to_peak)]
    result_2 = grouped.agg({
        'tip_pct': functions_2,
        'total_bill': functions_2
    })
    print(result_2)

    # grouping 컬럼들이 aggregate 결과에서 인덱스로 사용하지 않는 경우 (grouping 컬럼들을 인덱스로 사용하지 않는 경우)
    grouped = tips.groupby(['day', 'smoker'], as_index=False)
    print(grouped['tip'].mean())