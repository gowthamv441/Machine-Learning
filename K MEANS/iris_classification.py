from sklearn import cluster, datasets
import pandas as pd
iris = datasets.load_iris()
X_iris = iris.data

y_iris = iris.target

k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris,y_iris)

testSet = [[7.2, 3.6, 5.1, 2.5]]
test = pd.DataFrame(testSet)

print(k_means.predict(test))
