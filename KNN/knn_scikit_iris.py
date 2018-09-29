from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

data = pd.read_csv("Iris.csv")

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(data.iloc[:,0:4], data['Species'])

testSet = [[7.2, 3.6, 5.1, 2.5]]
test = pd.DataFrame(testSet)

print(neigh.predict(test))
