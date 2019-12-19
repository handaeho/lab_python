"""
선택 정렬 알고리즘
"""
import numpy as np

def find_min_max(numbers, reverse : bool):
    """
    리스트의 최소값과 최소값의 인덱스 / 최대값과 최대값의 인덱스를 리턴하는 함수
    :param numbers: 숫자 리스트
    :return: 최소값 & 최소값의 인덱스 or 최대값 & 최대값의 인덱스
    """
    if reverse is True: # reverse가 True. 즉, 내림차순 정렬
        max_id, max_val = 0, numbers[0]
        for i, v in enumerate(numbers):
            if v > max_val:
                max_id, max_val = i, v
        return max_id, max_val
    else:
        min_id, min_val = 0, numbers[0]
        for i, v in enumerate(numbers):
            if v < min_val:
                min_id, min_val = i, v
        return min_id, min_val


def sel_sort(numbers : list, reverse=False):
    """
    숫자 리스트를 전달 받아, 오름차순으로 정렬하는 함수
    :param numbers: 숫자 리스트
    :param reverse: False(오름차순), True(내림차순). Default = Flase
    :return: 오름차순으로 정렬된 리스트
    """
    numbers_copy = numbers.copy() # 원본 리스트 복사
    result = [] # 정렬된 결과가 저장될 리스트
    while numbers_copy: # numbers 원소가 있는 동안
        _, min_value = find_min_max(numbers_copy, reverse) # 위에서 선언한 find_min 함수
        # find_min 함수는 인덱스(min_id)와 값(min_val) 두개를 리턴하니까
        # '_'와 'min_value' 두개를 사용.
        result.append(min_value) # 리턴된 최소값과 그 인덱스를 result 리스트에 추가
        numbers_copy.remove(min_value) # 원본 배열에서는 이동된 원소를 제거.
        print('numbers = ', numbers)
        print('result = ', result)
        print('------------------------------')
    return result # 정렬된 리스트를 결과로 리턴

numbers = [np.random.randint(0, 100) for _ in range(10)]
sorted_num = sel_sort(numbers, reverse=True)
print('Fin_result = ', sorted_num)


# 이중 for문으로 선택  정렬 구현
def sel_sort2(numbers : list, reverse=False) -> None:
    """
    :param reverse: False(오름차순), True(내림차순). Default = Flase
    :param numbers:
    :return:
    """
    length = len(numbers)
    if reverse is False:
        for i in range(0, length-1): # i ~> 최소값을 저장해둘 위치
            for j in range(i+1, length): # j ~> 최소값을 찾기위해 비교할 대상이 되는 위치
                if numbers[i] > numbers[j]: # 현재 i보다 j가 작으면
                    numbers[i], numbers[j] = numbers[j], numbers[i] # i와 j 위치 변경.
                    print(numbers)
    else:
        for i in range(0, length-1):
            for j in range(i+1, length):
                if numbers[i] < numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    print(numbers)

print('=================================================')
numbers = [np.random.randint(0, 100) for _ in range(10)]
sel_sort2(numbers, reverse=True)

