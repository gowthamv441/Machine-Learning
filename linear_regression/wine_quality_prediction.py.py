from sklearn import linear_model
import pandas as pd
data = pd.read_csv("winequality-red.csv")

print (data.columns.values)

lm = linear_model.LinearRegression()
lm.fit(data.iloc[:,0:10], data['quality'])

testSet = [[7.4,0.7,0.0,1.9,0.076,11.0,34.0,0.9978,3.51,0.56]]
test = pd.DataFrame(testSet)

print (lm.predict(test))
