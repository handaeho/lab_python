"""
Scikit-learn 패키지를 이용한 Naive Bayes 알고리즘

Naive Bayes 분류기를 사용한 'nb_test.csv' 분류 및 예측
"""
import pandas as pd

# 데이터 셋 load
dataset = pd.read_csv('nb_test.csv', sep='\t')
print(dataset)
#   Weather      Car      Class
# 0   sunny  working     go-out
# 1   rainy   broken     go-out
# 2   sunny  working     go-out
# 3   sunny  working     go-out
# 4   sunny  working     go-out
# 5   rainy   broken  stay-home
# 6   rainy   broken  stay-home
# 7   sunny  working  stay-home
# 8   sunny   broken  stay-home
# 9   rainy   broken  stay-home

# 외출할 확률 P(go_out)
p_go_out = 5 / 10

# 집에 있을 확률 P(stay_home)
p_stay_home = 5 / 10 # P(stay_home) = 1 - P(go_out)

# 외출 했을 때, 날씨가 맑을 조건부 확률 P(sunny_when_go_out) = P(sunny|go_out)
# ~~~> P(sunny)의 확률에서 P(go_out)가 발생할 조건부 확률
p_sunny_when_go_out = 4 / 5

# 외출 했을 때, 비가 올 조건부 확률 P(rainy_when_go_out) = P(rainy|go_out)
# ~~~> P(rainy)의 확률에서 P(go_out)가 발생할 조건부 확률
p_rainy_when_go_out = 1 / 5

# 외출 했을 때, 자동차가 정상일 조건부 확률 P(working_when_go_out) = P(working|go_out)
# ~~~> P(working)의 확률에서 P(go_out)가 발생할 조건부 확률
p_working_when_go_out = 4 / 5

# 외출 했을 때, 자동차가 고장일 조건부 확률 P(broken_when_go_out) = P(broken|go_out)
# ~~~> P(broken)의 확률에서 P(go_out)가 발생할 조건부 확률
p_broken_when_go_out = 1 / 5

# 집에 있을 때, 날씨가 맑을 조건부 확률 P(sunny_when_stay_home) = P(sunny|stay_home)
# ~~~> P(sunny)의 확률에서 P(stay_home)가 발생할 조건부 확률
p_sunny_when_stay_home = 2 / 5

# 집에 있을 때, 비가 올 조건부 확률 P(rainy_when_stay_home) = P(rainy|stay_home)
# ~~~> P(rainy)의 확률에서 P(stay_home)가 발생할 조건부 확률
p_rainy_when_stay_home = 3 / 5

# 집에 있을 때, 자동차가 정상일 조건부 확률 P(working_when_stay_home) = P(working|stay_home)
# ~~~> P(working)의 확률에서 P(stay_home)가 발생할 조건부 확률
p_working_when_stay_home = 1 / 5

# 집에 있을 때, 자동차가 고장일 조건부 확률 P(broken_when_stay_home) = P(broken|stay_home)
# ~~~> P(broken)의 확률에서 P(stay_home)가 발생할 조건부 확률
p_broken_when_stay_home = 4 / 5

# 여기까지는 데이터를 기반으로 이미 알고있는 확률을 계산했다. ~~~> '사전 확률'
# 이제 만약 날씨와 자동차의 상태에 따라 외출하거나 집에 있을 확률을 모른다는 가정하에 확률을 계산해보자.

# ------------------------------------------------------------------------------------------------
# 베이즈 정리 : P(A|B) = P(A∩B) / P(B) = P(B|A)P(A) / P(B)
# 만약 A, B 두 사건이 동시에 발생 했을 때, X가 일어나는 조건부 확률을 베이즈 정리로 나타내면
# P(X|A, B) = P(A, B|X) * P(X) / P(A, B)

# Navie Bayes : 데이터 세트의 모든 변수들은 서로 독립적이라고 가정.
# P(A, B|X) = P(A|X) * P(B|X) ~~~> 사건 A, B와 X를 '독립적'이라고 가정했기 때문
# 따라서 Navie Bayes에 의해 P(X|A, B) ~ P(A|X) * P(B|X) * P(X)로 나타낼수 있다.
#   알아내고 싶은 확률 ~ 사전에 계산한 사전 확률

# Navie Bayes 예측 알고리즘 => 확률들을 같은 조건에서 Navie Bayes 가정 하에 계산하고, 더 큰 값으로 예측을 한다.
# ------------------------------------------------------------------------------------------------

# Navie Bayes로 원하는 확률 계산

# 날씨가 맑고 자동차가 정상일 때, 외출할 확률 P(go_out|sunny, working)
# P(go_out|sunny, working) ~ P(sunny|go_out) * P(working|go_out) * P(go_out)
p_go_out_when_sunny_working = p_sunny_when_go_out * p_working_when_go_out * p_go_out
print('P(go_out|sunny, working) = ', p_go_out_when_sunny_working)
# P(go_out|sunny, working) = 0.32000000000000006

# 날씨가 맑고 자동차가 정상일 때, 집에 있을 확률 P(stay_home|sunny, working)
# P(stay_home|sunny, working) ~ P(sunny|stay_home) * P(working|stay_home) * P(stay_home)
p_stay_home_when_sunny_working = p_sunny_when_stay_home * p_working_when_stay_home * p_stay_home
print('P(stay_home|sunny, working) = ',p_stay_home_when_sunny_working)
# P(stay_home|sunny, working) = 0.04000000000000001

# 날씨가 비가 오고, 자동차가 정상일 때, 외출할 확률 P(go_out|rainy, working)
# P(go_out|rainy, working) ~ P(rainy|go_out) * P(working|go_out) * P(go_out)
p_go_out_when_rainy_working = p_rainy_when_go_out * p_working_when_go_out * p_go_out
print('P(go_out|rainy, working) = ', p_go_out_when_rainy_working)
# P(go_out|rainy, working) =  0.08000000000000002

# 날씨가 비가 오고, 자동차가 정상일 때, 집에 있을 확률 P(go_out|rainy, working)
# P(stay_home|rainy, working) ~ P(rainy|stay_home) * P(working|stay_home) * P(stay_home)
p_stay_home_when_rainy_working = p_rainy_when_stay_home * p_working_when_stay_home * p_stay_home
print('P(stay_home|rainy, working) = ', p_stay_home_when_rainy_working)
# P(stay_home|rainy, working) =  0.06

# 날씨가 맑고 자동차가 고장일 때, 외출할 확률 P(go_out|sunny, broken)
# P(go_out|sunny, broken) ~ P(sunny|go_out) * P(broken|go_out) * P(go_out)
p_go_out_when_sunny_broken = p_sunny_when_go_out * p_broken_when_go_out * p_go_out
print('P(go_out|sunny, broken) = ', p_go_out_when_sunny_broken)
# P(go_out|sunny, broken) =  0.08000000000000002

# 날씨가 맑고 자동차가 고장일 때, 집에 있을 확률 P(stay_home|sunny, broken)
# P(stay_home|sunny, broken) ~ P(sunny|stay_home) * P(broken|stay_home) * P(stay_home)
p_stay_home_when_sunny_broken = p_sunny_when_stay_home * p_broken_when_stay_home * p_stay_home
print('P(stay_home|sunny, broken) = ', p_stay_home_when_sunny_broken)
# P(stay_home|sunny, broken) =  0.16000000000000003

# 날씨가 비가 오고, 자동차가 고장일 때, 외출할 확률 P(go_out|rainy, broken)
# P(go_out|rainy, broken) ~ P(rainy|go_out) * P(broken|go_out) * P(go_out)
p_go_out_when_rainy_broken = p_rainy_when_go_out * p_broken_when_go_out * p_go_out
print('P(go_out|rainy, broken) = ', p_go_out_when_rainy_broken)
# P(go_out|rainy, broken) =  0.020000000000000004

# 날씨가 비가 오고, 자동차가 고장일 때, 집에 있을 확률 P(stay_home|rainy, broken)
# P(stay_home|rainy, broken) ~ P(rainy|stay_home) * P(broken|stay_home) * P(stay_home)
p_stay_home_when_rainy_broken = p_rainy_when_stay_home * p_broken_when_stay_home * p_stay_home
print('P(stay_home|rainy, broken) = ', p_stay_home_when_rainy_broken)
# P(stay_home|rainy, broken) =  0.24







