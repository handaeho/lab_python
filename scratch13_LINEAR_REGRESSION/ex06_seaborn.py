"""
Seaborn 시각화 패키지
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_boston


# boston data load
boston = load_boston()
X = boston.data
y = boston.target
features = boston['feature_names']

# load 된 데이터(np.ndarray 타입)를 pandas.DataFrame으로
boston_df = pd.DataFrame(X, columns=features)
print(boston_df.head())

# boston_df에 Price(target) 컬럼 추가
boston_df['Price'] = y
print(boston_df.head())
print(boston_df.shape)

# 필요 컬럼 및 데이터 추출
columns = ['LSTAT', 'INDUS', 'NOX', 'RM', 'Price']
subset_df = boston_df[columns]
print(subset_df.head())

# seaborn 시각화 패키지 사용
sns.pairplot(subset_df)
plt.show()

# 상관 행렬(Correlation Matrix) : 상관 계수들로 이루어진 행렬
corr_matrix = subset_df.corr().round(2) # .corr() ~~> 상관계수 계산 함수
print(corr_matrix)
#        LSTAT  INDUS   NOX    RM  Price
# LSTAT   1.00   0.60  0.59 -0.61  -0.74
# INDUS   0.60   1.00  0.76 -0.39  -0.48
# NOX     0.59   0.76  1.00 -0.30  -0.43
# RM     -0.61  -0.39 -0.30  1.00   0.70
# Price  -0.74  -0.48 -0.43  0.70   1.00

# seaborn.heatmap() : 상관 계수가 클수록 '더 진한 색'으로 표시된다.
sns.heatmap(corr_matrix, annot=True) # 'annot=True' ~> heatmap에 상관 계수를 표시한다.(default False)
plt.show()


