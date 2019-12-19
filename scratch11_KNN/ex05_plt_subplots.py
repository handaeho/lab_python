"""
한 화면에서 여러개의 plot를 출력 해보자
"""
import matplotlib.pyplot as plt
import pandas as pd

col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']
iris = pd.read_csv('iris.csv', header=None, names=col_names)

iris_by_class = iris.groupby(by='Class')

xy = [] # x축과 y축에 사용할 변수들을 저장(변수들을 조합)
for i in range(4):
    for j in range(i+1, 4):
        xy.append((col_names[i], col_names[j]))
print(xy) # [('sepal_length', 'sepal_width'), ('sepal_length', 'petal_length'), ('sepal_length', 'petal_width'), ...

fig, ax = plt.subplots(2, 3) # ~~~> 한 화면을 2 x 3으로 나누겠다. (그래프는 ax(축)에 따라 그리게 됨)
xy_idx = 0
for row in range(2): # 행은 2개
    for col in range(3): # 열은 3개
        axis = ax[row, col] # == axis = ax[row][col]
        x = xy[xy_idx][0]
        y = xy[xy_idx][1]
        xy_idx += 1
        axis.set_title(f'{x} vs {y}') # subplot 제목
        axis.set_xlabel(x) # subplot의 x축 label
        axis.set_ylabel(y) # subplot의 y축 label
        for name, group in iris_by_class:
            axis.scatter(group[x], group[y], label=name)
plt.legend()
plt.show()


