"""
1) R의 ggplot2 패키지에 포함된 mpg 데이터 프레임을 csv 파일 형식으로 저장
2) 저장된 csv 파일을 파이썬 프로젝트의 scratch08_경사하강법 폴더에 복사
3) 저장된 csv 파일을 읽어서 배기량(displ)과 시내 연비(cty) 데이터를 추출
4) 선형 회귀식 cty = slope * displ + intersect 의 기울기(slope)와 절편(intersect)을
경사 하강법의 3가지 방법(stochastic, batch, mini-batch)으로 결정하고 값을 비교
5)배기량과 시내 연비 산점도 그래프(scatter plot)과 선형 회귀 직선을 하나의 plot으로 출력해서 결과 확인
"""
import csv
import random
import matplotlib.pyplot as plt

from scratch04_벡터및행렬연산.ex01 import vector_mean
from scratch08_경사하강법.ex03 import gradient_step
from scratch08_경사하강법.ex04 import linear_gradient, minibatches

input_file = "mpg.csv"
output_file = "mpg_ex.csv"

select_col = [3, 8]

# with open(input_file, 'r', newline='') as in_file:
#     with open(output_file, 'w', newline='') as out_file:
#         freader = csv.reader(in_file)
#         fwriter = csv.writer(out_file)
#         next(freader)
#         for row_list in freader:
#             row_list_output = []
#             for index_value in select_col:
#                 row_list_output.append(row_list[index_value])
#             print(row_list_output)
#             fwriter.writerow(row_list_output)

dataset = []
with open('mpg_ex.csv', 'r') as data:
    data.readline()
    for line in data:
        dataset.append(line.strip().split(','))

for i in range(len(dataset)):
    for j in range(len(dataset[0])):
        dataset[i][j] = float(dataset[i][j])
print(dataset) # [[1.8, 21.0], [2.0, 20.0], [2.0, 21.0], [2.8, 16.0], [2.8, 18.0], [3.1, 18.0], ...]

xs = []
ys = []
for i in dataset:
    # 그래프를 그리기 위해 dataset의 1 ~ n번째 원소 리스트의 각 0번지 값을 x, 1번지 값을 y로
   xs.append(i[0])
   ys.append(i[1])
print(xs) # [1.8, 2.0, 2.0, 2.8, 2.8, 3.1, 1.8, 1.8, 2.0, 2.0, 2.8, 2.8, ...]
print(ys) # [21.0, 20.0, 21.0, 16.0, 18.0, 18.0, 18.0, 16.0, 20.0, 19.0, ...]


print('=== 확률적 경사 하강법 ===')
theta = [1, 1]  # [기울기, 절편], y = x + 1
step = 0.001  # 파라미터의 값을 변경 할 때 사용할 가중치(학습률)

for epoch in range(200):  # 임의의 횟수(epoch)만큼 반복
    random.shuffle(dataset)
    # 각각의 epoch마다 dataset에서 샘플(x, y)를 추출.
    for x, y in dataset:
        # 각 점에서 gradient 계산
        gradient = linear_gradient(x, y, theta)
        # 파라미터 theta(기울기, 절편)를 변경
        theta = gradient_step(theta, gradient, -step)  # 최소화 문제이므로 step는 '-'

    if (epoch + 1) % 10 == 0:  # 10번마다 출력해보자.
        print(f'{epoch} : {theta}')
    # === 확률적 경사 하강법 ===
    # # 9 : [2.204274078634416, 7.349838643539135]
    # # 19 : [0.968624283432864, 11.665794732341263]
    # # 29 : [0.03468448991572707, 14.981234617309983]
    # # ...
    # # 179 : [-2.556360783955486, 25.85391136578081]
    # # 189 : [-2.639925956097442, 25.88398372962143]
    # # 199 : [-2.691235726912461, 25.908428747362304]

print('\n=== 배치 경사 하강법 ===')
step = 0.01 # 학습률
theta = [1, 1]  # 임의의 값으로 [기울기, 절편] 설정
for epoch in range(5000):
    # 모든 샘플에서의 gradient를 계산
    gradients = [linear_gradient(x, y, theta) for x, y in dataset]
    # gradients의 평균을 계산
    gradient = vector_mean(gradients)
    # 파라미터 theta(기울기, 절편)을 변경
    theta = gradient_step(theta, gradient, -step)
    if (epoch + 1) % 100 == 0:
        print(f'{epoch}: {theta}')
    # === 배치 경사 하강법 ===
    # 99: [2.9093384056866447, 4.267702751879657]
    # 199: [2.3149123748644227, 6.599502383809822]
    # 299: [1.7841057146350183, 8.681736261430764]
    # ...
    # 4799: [-2.617478264487578, 25.94814974720132]
    # 4899: [-2.6203856185736862, 25.959554636449916]
    # 4999: [-2.622981807077627, 25.969738893846493]

print(' \n === 미니 배치 하강법 ===')
step = 0.01 # 학습률
theta = [1, 1] # 임의의 파라미터 시작 값
for epoch in range(1000):
    mini_batchs = minibatches(dataset, 20, True)
    for batch in mini_batchs:
        gradients = [linear_gradient(x, y, theta) for x, y in batch]
        gradient = vector_mean(gradients)
        theta = gradient_step(theta, gradient, -step)
    if (epoch + 1) % 100 == 0:
        print(f'{epoch} : {theta}')
    # === 미니 배치 하강법 ===
    # 99 : [-1.0564020417874882, 19.782682691916353]
    # 199 : [-2.2327651956013055, 24.45385767319586]
    # 299 : [-2.563323724411359, 25.638506507946243]
    # ...
    # 799 : [-2.622227770710156, 26.051242236142972]
    # 899 : [-2.6096459774186496, 26.062486752172138]
    # 999 : [-2.634286621026318, 26.053602279285556]

plt.scatter(xs, ys)
plt.show()




