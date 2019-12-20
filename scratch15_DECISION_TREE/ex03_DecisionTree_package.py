"""
패키지를 사용하여 iris를 Decision Tree로 분류 및 예측
"""
import graphviz
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz

# 데이터 load
iris = load_iris()
X = iris.data # ~> 데이터(샘플 2차원 리스트(행렬))
y = iris.target # ~> 타겟(품종)

# 데이터 셋을 train_set / test_set으로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# DecisionTreeClassifier() 객체 생성
decision_tree = DecisionTreeClassifier()

# 데이터를 모델에 fitting(학습)
decision_tree.fit(X_train, y_train)

# 예측
y_pred = decision_tree.predict(X_test)
print('Real : ', y_test)
print('Predict : ', y_pred)

# 구성된 의사 결정 트리 출력
text_result = export_text(decision_tree, iris.feature_names)
print(text_result)

# 구성된 의사 결정 트리를 그래프를 사용해 시각화
graph_data = export_graphviz(decision_tree,
                             feature_names=iris.feature_names, # ~> 데이터의 label 이름 사용
                             class_names=iris.target_names, # ~> 타겟 이름 사용
                             filled=True,
                             special_characters=True) # 그래프를 그릴 데이터 생성
graph = graphviz.Source(graph_data) # 그래프 객체
graph.render('iris') # 그래프 객체를 렌더링 해, pdf 파일로 작성
# ~> 단, 사전에 웹에서 'graphviz-2.38.msi'의 설치 후, 설치된 경로를 시스템 환경 변수의 'PATH'로 설정해야 한다.


