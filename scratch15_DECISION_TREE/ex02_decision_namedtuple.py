"""
Decision Tree

= NamedTuple을 상속받는 클래스를 이용해 면접자(Candidate)들의 스펙을 정리하고,
각 스펙에 따라 합격 여부를 조사해 어떤 스펙이 합격에 영향을 미쳤는지 알아보자.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

from collections import namedtuple, Counter, defaultdict
from typing import NamedTuple


# Candidate = namedtuple('Candidate', ('level', 'lang', 'tweets', 'phd', 'result'))
# ~> 클래스 선언 방식은 이 방식과 결과는 같지만 이 방법에서는 default를 설정 할 수 없다.

class Candidate(NamedTuple):
    """ NamedTuple을 상속받는 클래스 선언 """
    level: str
    lang: str
    tweets: bool
    phd: bool
    result: bool=None # field의 default 설정


def uncertainty(p):
    """
    0 <= p <= 1
    p = 0이면, 항상 발생하지 않는다고 '확신'할 수 있다. 즉, 불확실성이 없다.
    또한, p = 1이면, 항상 발생한다고 '확신'할 수 있다. 즉, 불확실성이 없다.
    그러나 0 < p < 1이면, 발생할 수도, 발생하지 않을수도 있다. 즉, 불확실성이 있다.
    """
    return -p * math.log(p, 2)


def entropy(class_probabilities):
    """
    주어진 확률들의 리스트에 대해서 '엔트로피'를 계산
    E = sum(i)[uncertainty(p_i)] = (-p_1 * math.log(p_1)) + (-p_2 * math.log(p_2)) + ...

    엔트로피 : 불확실한 정도
    불확실성이 크다 ~~~> 엔트로피가 크다.
    불확실성이 작다 ~~~> 엔트로피가 작다.
    즉, '확실하다'면 '엔트로피'는 '0'이다(없다).
    """
    ent = 0
    for p in class_probabilities:
        ent += uncertainty(p)

    return ent


def binary_entropy(p):
    """
    사건이 발생할 확률 p, 발생하지 않을 확률 1-p
    Entropy = (-p * log(p)) + (-(1-p) * log(1-p))
    """

    return uncertainty(p) + uncertainty(1-p)


def class_probabilities(labels):
    """
    Candidate의 합/불합을 예측하기 위해, 어떤 스펙을 선택해 의사를 결정할 지 판별
    따라서 각 스펙(label)의 확률을 계산
    """
    total_count = len(labels)
    counts = Counter(labels) # Counter() ~> {label_1: cnt_1, label_2: cnt_2, ...} dict와 비슷하고 개수를 세준다.
    print(counts)
    probabilities = []
    for count in counts.values():
        p = count / total_count # 각 label의 확률
        probabilities.append(p)
    # probabilities = [count/total_count for count in counts.values()]

    return probabilities


def partition_by(dataset, attr_name):
    """
    NamedTuple들의 리스트로 이루어진 dataset을
    NamedTuple의 특정 attribute(label)별로 파티셔닝을 하자.
    (label 별로 dataset의 data를 분할)
    """
    partitions = defaultdict(list) # list를 value로 갖는 dict
    for sample in dataset:
        # 해당 attr_name의 값을 찾아서 dict의 key로 sample을 저장한다.
        key = getattr(sample, attr_name) # getattr ~> attribute를 가져온다.
        partitions[key].append(sample)

    return partitions


def partition_entropy_by(dataset, by_partition, by_entropy):
    """
    by_partition으로 분리된 각 파티션에서 by_entropy를 기준으로 엔트로피를 각각 계산하고,
    파티션 내에서의 (엔트로피 * 파티션 비율)의 sum을 리턴.

    by_partition : 파티셔닝을 할 기준
    by_entropy : 엔트로피를 구할 기준

    by_partition으로 나누어진 그룹 중에서 by_entropy가 True / False를 파악하고, 그 확률을 계산한다.
    그리고 확률. 즉, 엔트로피에 그 그룹의 비율을 곱해서 모두 더해 리턴하는 함수.
    ---> ((엔트로피 * 파티션 비율)의 sum)
    이렇게 구해진 엔트로피는 'by_partition'으로 들어온 레이블이 'by_entropy' 레이블에 대해 갖는 엔트로피가 된다.

    ex) partition_entropy_by(candidates, 'level', 'result')
    ~> 지원자들을 level별로 파티션으로 나누어, 그 그룹별로 합격한 사람이 누구인가?(True / False로 나타남)
        그렇다면, 파티셔닝된 그룹별 합격(True)의 확률은 어떻게 되는가? 즉, 엔트로피는 어떻게 되는가?
        그리고 그 엔트로피에 그 그룹의 비율을 곱하고 모두 더해 전체 엔트로피를 구하고 리턴하자.
    """
    # 데이터셋을 파티셔닝
    partitions = partition_by(dataset, by_partition)
    # 각 label의 리스트 생성(각 label별 확률 계산 위함)
    labels = []
    for partition in partitions.values(): # 각 파티션에 속한 sample들의 개수만큼 반복
        # 각 파티션에 속한 샘플들을 찾아서
        values = []
        for sample in partition: # 파티션의 원소 개수만큼
            values.append(getattr(sample, by_entropy)) # by_entropy을 attribute로 가져온다.
        labels.append(values)
    print(labels)
    # 각 파티션이 차지하는 비율을 계산하고, 각 파티션의 엔트로피에 그 비율을 곱해주기 위해서
    total_count = sum(len(label) for label in labels) # 총 label 개수(Senior 5개, Mid 4개, Junior 5개)
    ent = 0
    for label in labels:
        cls_prob = class_probabilities(label) # 파티션 당, 레이블 별 확률 계산
        part_ent = entropy(cls_prob) # 파티션 당, 엔트로피 계산
        ent += part_ent * (len(label) / total_count)
        # ~> 전체 엔트로피 = sum(그룹당 엔트로피 * 레이블의 확률)
        # 이 전체 엔트로피는 그 레이블이 어떤 레이블에 대해 갖는 엔트로피를 의미한다.

    return ent


if __name__ == '__main__':
    candidates = [Candidate('Senior', 'Java', False, False, False),
                  Candidate('Senior', 'Java', False, True, False),
                  Candidate('Mid', 'Python', False, False, True),
                  Candidate('Junior', 'Python', False, False, True),
                  Candidate('Junior', 'R', True, False, True),
                  Candidate('Junior', 'R', True, True, False),
                  Candidate('Mid', 'R', True, True, True),
                  Candidate('Senior', 'Python', False, False, False),
                  Candidate('Senior', 'R', True, False, True),
                  Candidate('Junior', 'Python', True, False, True),
                  Candidate('Senior', 'Python', True, True, True),
                  Candidate('Mid', 'Python', False, True, True),
                  Candidate('Mid', 'Java', True, False, True),
                  Candidate('Junior', 'Python', False, True, False)]

    # uncertainty() 함수 그래프
    x_pts = np.linspace(0.0001, 1, 100) # 0.0001 ~ 1의 범위를 100개로 분할, 포인트 x 생성
    y_pts = [uncertainty(p) for p in x_pts] # 함수 uncertainty()의 x에 따른 y
    plt.plot(x_pts, y_pts)
    plt.xlim(0.0) # 0 <= x만 그래프로
    plt.ylim(0.0) # 0 <= y만 그래프로
    plt.title('f(x) = -p * log(p)')
    plt.show()

    # binary_entropy() 함수 그래프
    x_pts = np.linspace(0.0001, 0.9999, 100)
    y_pts = [binary_entropy(p) for p in x_pts]
    plt.plot(x_pts, y_pts)
    plt.xlim(0.0)
    plt.ylim(0.0)
    plt.axvline(x=0.5, color='0.75')
    plt.title('binary_entropy')
    plt.show()

    # entropy() 함수 테스트
    rain_prob = [1] # 비가 반드시 온다.
    ent = entropy(rain_prob)
    print('entropy = ', ent) # entropy =  0.0

    rain_prob = [0.5, 0.5] # 비가 올 확률 0.5, 안 올 확률 0.5
    ent = entropy(rain_prob)
    print('entropy = ', ent) # entropy =  1.0

    rain_prob = [0.9, 0.1] # 비가 올 확률 0.9, 안 올 확률 0.1
    ent = entropy(rain_prob)
    print('entropy = ', ent) # entropy =  0.4689955935892812

    # class_probabilities() 함수 테스트
    level = ['Junior', 'Senior', 'mid', 'Junior']
    # P('Junior') = 2/4, P('Senior') = 1/4, P('Mid') = 1/4
    cls_prob = class_probabilities(level)
    print(cls_prob)
    # Counter({'Junior': 2, 'Senior': 1, 'mid': 1})
    # [0.5, 0.25, 0.25]

    # partition_by() 함수 테스트
    partition_by_level = partition_by(candidates, 'level')
    print('partition_by_level = ', partition_by_level)

    partition_by_tweets = partition_by(candidates, 'tweets')
    print('partition_by_tweets = ', partition_by_tweets)

    # partition_entropy_by() 함수
    ent_level = partition_entropy_by(candidates, 'level', 'result')
    print(ent_level)
    # [[False, False, False, True, True], [True, True, True, True], [True, True, False, True, False]]
    # Counter({False: 3, True: 2}) ~~~> 'Senior' 파티션에서 F=3, T=2(불합격 3명, 합격 2명)
    # Counter({True: 4}) ~~~> 'Mid'파티션에서 T=4(합격 4명)
    # Counter({True: 3, False: 2}) ~~~> 'Junior' 파티션에서 T=3, F=2(합격 3명, 불합격 2명)
    # 0.6935361388961918 ~~~> 'level'이 'result'에 대해 갖는 엔트로피

    ent_lang = partition_entropy_by(candidates, 'lang', 'result')
    print(ent_lang)
    # [[False, False, True], [True, True, False, True, True, True, False], [True, False, True, True]]
    # Counter({False: 2, True: 1}) # ~~~> 'Java' 파티션에서 합격 2명 불합격 1명
    # Counter({True: 5, False: 2}) # ~~~> 'Python' 파티션에서 합격 5명, 불합격 2명
    # Counter({True: 3, False: 1}) # ~~~> 'R' 파티션에서 합격 3명, 불합격 1명
    # 0.8601317128547441 ~~~> 'lang'가 'result'에 대해 갖는 엔트로피

    ent_tweets = partition_entropy_by(candidates, 'tweets', 'result')
    print(ent_tweets)
    # [[False, False, True, True, False, True, False], [True, False, True, True, True, True, True]]
    # Counter({False: 4, True: 3}) ~~~> 트위터를 안 하는 사람 파티션에서 불합격 4명, 합격 3명
    # Counter({True: 6, False: 1}) ~~~> 트위터를 하는 사람 파티션에서 합격 6명, 불합격 1명
    # 0.7884504573082896 ~~~> 'tweets'가 'result'에 대해 갖는 엔트로피

    ent_phd = partition_entropy_by(candidates, 'phd', 'result')
    print(ent_phd)
    # [[False, True, True, True, False, True, True, True], [False, False, True, True, True, False]]
    # Counter({True: 6, False: 2}) ~~~> 박사학위가 없는 사람 파티션에서 합격 6명, 불합격 2명
    # Counter({False: 3, True: 3}) ~~~> 박사학위가 있는 사람 파티션에서 불합격 3명, 합격 3명
    # 0.8921589282623617 ~~~> 'phd'가 'result'에 대해 갖는 엔트로피










