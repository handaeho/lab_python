"""
Decision Tree

= NamedTuple을 상속받는 클래스를 이용해 면접자(Candidate)들의 스펙을 정리하고,
각 스펙에 따라 합격 여부를 조사해 어떤 스펙이 합격에 영향을 미쳤는지 알아보자.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

from collections import namedtuple, Counter, defaultdict
from typing import NamedTuple, Any


# Candidate = namedtuple('Candidate', ('level', 'lang', 'tweets', 'phd', 'result'))
# ~> 클래스 선언 방식은 이 방식과 결과는 같지만 이 방법에서는 default를 설정 할 수 없다.

class Candidate(NamedTuple):
    """ NamedTuple을 상속받는 Candidate 클래스 선언 """
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


class Leaf(NamedTuple):
    """ NamedTuple을 상속받는 잎 노드(터미널 노드) 클래스 선언 """
    value: Any


class Split(NamedTuple):
    """ NamedTuple을 상속받는 Split(트리에서 가지가 분기되는 기준)클래스 선언 """
    attribute: str
    subtree: dict


def predict(model, sample):
    """ 우리가 구현한 의사결정나무 모델로 sample 지원자의 합격/불합격을 예측 """
    if isinstance(model, Leaf): # model이 Leaf() 상태라면 (터미널 노드에 도달했으면)
        return model.value # model의 value(합격(True)/불합격(False))을 리턴한다.

    subtree_key = getattr(sample, model.attribute)
    print('subtree_key : ', subtree_key)
    # sample에서 model(트리)의 attribute를 꺼내어 subtree의 key로 사용한다.
    # ~> 만약, 모델의 attribute가 'level'이면, sample에서 'Senior' 또는 'Mid', 'Junior'를 꺼낸다.
    # 왜냐? subtree가 아닌 경우, 가지를 따라 분기해야 하기 떄문에
    # sample이 attribute로 가지고 있는 값을 찾아서 해당 가지로 내려간다.

    subtree = model.subtree[subtree_key]
    # subtree_key로 모델에서 subtree를 찾아 가겠다.
    # 만약, key가 'Senior'면 'Senior'를 기준으로 분기되어 생성된 트리로 가겠다.

    return predict(subtree, sample)
    # 재귀함수로 자기 자신인 predict()를 다시 호출해,
    # 다시 model에 subtree를, sample에 sample을 다시 넣고 탐색.


def build_tree(dataset, by_splits, target):
    """
    예측을 위한 데이터의 tree 모델 생성
    dataset : 예측의 대상이 될 데이터 세트
    by_splits : 분기의 기준이 될 label(attribute)
    target : 알아내고자 하는 결과 (합격(True) / 불합격(False))
    """
    print('\n >>> Building Tree ... <<<')
    print(f'len(dataset) : {len(dataset)} / dataset : {dataset}')
    print(f'by_splits는 {by_splits} / target은 {target}')

    # target의 개수를 카운트 {True(합격): x명, False(불합격): y명}
    target_counts = Counter(getattr(sample, target) for sample in dataset)
    print(f'target_counts = {target_counts}') # target_counts = Counter({True: 9, False: 5})
    # ~> sample의 target이 True인지 False인지를 가져와서 카운트 (현재 Counter() 객체의 len은 2)

    # Counter() 객체 생성해, len(Counter) == 1이면 터미널노드가 되므로(결과가 1개뿐이므로) Leaf()를 생성하고 종료.
    if len(target_counts) == 1:
        keys = list(target_counts.keys())
        # dict 타입의 keys()가 리턴하는 타입은 리스트가 아니기 때문에 '[] 연산자'는 사용 불가.
        result = keys[0] # ~> True 또는 False 중 하나
        leaf = Leaf(result)
        print('leaf : ', leaf)
        return leaf

    # len(by_splits) == 0이면, 트리의 깊이(depth)가 0. 즉, 더이상 서브트리를 나눌 기준이 없을 때,
    if not by_splits: # if len(by_splits) == 0
        return Leaf(list(target_counts.keys())[0]) # ~> 남은 분할 기준은 터미널 노드가 되고, 이를 리턴한다.

    # len(Counter) != 1이면 터미널 노드가 아니므로 특정 label로 파티션을 나눌수 있다.
    # by_split(분기의 기준)의 각 변수로 파티션을 구성하고, 파티션 별로 엔트로피를 계산하여
    # 엔트로피가 가장 낮은(불확실성이 작은) 변수를 선택한다.

    # 먼저 partition_entropy_by(dataset, by_split, by_entropy)를 호출 할 수 있는 'Wrapper(helper) 함수' 작성
    def splitted_entropy(split_attr):
        result = partition_entropy_by(dataset, split_attr, target)
        print('Splitted entropy = ', result)
        return result
    best_splitter = min(by_splits, key=splitted_entropy)
    print('best_splitted = ', best_splitter)
    # ~~~> min, max, sort등의 함수는 전달받은 리스트에서 key를 이용해 그 결과를 찾는데,
    # key에 partition_entropy_by(dataset, split_attr, target) 함수를 주기 위해서는 파라미터를 3개 전달해야 한다.
    # 그러나 우리는 'by_splits' 리스트 하나만 가지고 있으므로 파라미터를 1개만 줄 수 있다.
    # 따라서 'Wrapper 함수'로 '감싸주어서' 파라미터 1개를 전달해주고,
    # 나머지 2개의 파라미터는 이미 가지고 있는 변수를 사용할 수 있게하고,
    # 그 Wrapper 함수의 리턴값을 'key'로 하여 min(by_splits) 함수를 실행한다.
    # 즉, 'by_splits' 리스트가 'splitted_entropy(split_attr)'로 들어가고,
    # 그 안에서 'partition_entropy_by(dataset, split_attr, target)'가 실행되어 결과를 리턴하면 그 결과값이 key가 되는것.
    # 그리고 그 key로 'by_splits'의 최소값을 찾는다.

    # 그리고 이렇게 선택된 변수(엔트로피가 최소인 변수)로 파티션을 구성하고,
    partitions = partition_by(dataset, best_splitter)
    print('partitions : ', partitions)
    # ~> 엔트로피가 가장 낮은 'level'에 따라서 파티션을 나눈것을 확인 할 수 있다.

    # 그 변수를 제외한 나머지 변수들로 다음 트리를 구성하게 됨.(위 과정 반복)
    # 먼저, branch 기준 리스트에서 선택된 변수 제거
    new_split = [x for x in by_splits if x != best_splitter]
    # ~> 'best_splitted'로 사용되지 않은 변수들만 'new_split' 리스트에 추가
    print(f'제거 전 by_splits : {by_splits}, 제거 후 new_split : {new_split}')

    subtree = {k: build_tree(subset, new_split, target) for k, subset in partitions.items()}
    # ~> build_tree() 함수에 다음 트리 구조와 새로운 분기 조건, target을 사용해 재귀 호출하고,
    # 다음 트리(subtree)를 구성

    # Split 객체를 생성하고 리턴 ~~~> 다음 분기 조건이 된다.
    return Split(best_splitter, subtree)


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

    # leaf 클래스 / Split 테스트
    hire_tree = Split('level', {'Senior': Split(
                                    'tweets',
                                    {True: Leaf(True), False: Leaf(False)}),
                                'Mid': Leaf(True),
                                'Junior': Split(
                                    'phd',
                                    {True: Leaf(False), False: Leaf(True)}
                                )})
    # 우리가 구성한 'Candidate'의 스펙으로 보면 'level'이라는 label(attribute)에서,
    # 'Senior', 'Junior'라는 분기 기준으로 분기하게 되면,
    # 각각 다시 'tweets', 'phd'라는 노드로 갈라지게 되므로 Split() 클래스를 value로 갖고,
    # 'Mid'라는 기준으로 분기하면 바로 터미널 노드가 되므로(합격(True)이므로) Leaf() 클래스를 value로 갖는다.

    # 'Senior'의 tweets' 분기 기준 역시 True(사용O)/False(사용x)라는 기준으로 갈라지게 되므로 또 Split() 클래스를 갖는다.
    # 그리고 True라면 합격, False라면 불합격이므로 {True: Leaf(True), False: Leaf(False)}를 dict로 갖는다.

    # 'Junior'의 'phd; 분기 기준 역시 True(있다)/False(없다)라는 기준으로 갈라지므로 Split() 클래스를 갖고,
    # True라면 불합격, False라면 합격이므로 {True: Leaf(False), False: Leaf(True)}를 dict로 갖는다.

    # predict() 함수 테스트
    print(hire_tree)
    candidate_1 = Candidate('Senior', 'Java', False, False, False)
    result = predict(hire_tree, candidate_1)
    print('candidate_1 result = ', result)

    print(hire_tree)
    candidate_2 = Candidate('Mid', 'Python', False, False, True)
    result = predict(hire_tree, candidate_2)
    print('candidate_2 result = ', result)

    # build_tree 함수 테스트
    tree = build_tree(candidates, ['level', 'lang', 'tweets', 'phd'], 'result')
    # ~> candidate의 데이터 셋을 ['level', 'lang', 'tweets', 'phd']를 기준으로 트리를 구성하여 'result'를 알아보겠다.
    print(tree)