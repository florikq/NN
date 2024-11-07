from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()

iris_frame = pd.DataFrame(iris.data)

iris_frame.columns = iris.feature_names

iris_frame['target'] = iris.target

iris_frame['name'] = iris_frame.target.apply(lambda x: iris.target_names[x])

print(iris_frame)