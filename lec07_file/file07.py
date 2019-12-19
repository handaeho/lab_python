"""
file.readline() 메소드를 사용한 csv 파일 읽기
"""
def my_csv_reader(fn: str, header=True) -> list:
    """
    csv 파일의 데이터를 2차원 행렬 형태로 리턴하는 함수

    :param fn: 읽을 파일 이름(예 - data\\exam.csv)
    :param header: csv 파일의 header 존재 여부
    :return: csv 파일에서 header는 제외한 데이터로 이루어진 2차원 리스트
    """
    list_exam = []
    with open('exam.csv', mode='r', encoding='utf-8') as fn:
        fn.readline()
        for line in fn:
            list_exam.append(line.strip().split(','))

    exam_x = []
    for i in list_exam:
        for j in i:
            exam_x.append(int(j))
    n = 5
    exam_x = [exam_x[i * n:(i + 1) * n] for i in range((len(exam_x) + n - 1) // n)]

    return exam_x

def print_data(data: list) -> None:
    """
    2차원 리스트 내용 출력
    1 10 20 30 40
    2 11 21 31 41
    3 12 22 32 42
    ...

    :param data: 2차원 행렬 형태의 리스트
    :return: None
    """
    for i in data:
        print(i)

def get_sum_mean(data: list, col: int) -> tuple:
    """
    주어진 2차원 리스트에서 해당 컬럼 데이터들의 총합과 평균을 계산해 리턴

    :param data: 2차원 행렬 형태의 리스트
    :param col: 컬럼 인덱스(0, 1, 2, ...)
    :return: 컬럼 데이터의 합, 평균
    """
    sum_mean_list = []
    for i in data:
        sum_mean_list.append(i[col])
    sum_a = sum(sum_mean_list)
    avg_a = sum_a / len(sum_mean_list)

    print('해당 컬럼의 합계 = ', sum_a)
    print('해당 컬럼의 평균 = ', avg_a)

    return sum_a, avg_a

if __name__ == '__main__':
    d = my_csv_reader('data\\exam.csv')
    print_data(d)
    get_sum_mean(d, 0)
