import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Customers.csv')

data

import seaborn as sn

sn.jointplot(fd['Time on Website' ],fd['Yearly Amount Spent'])
sn.jointplot(fd['Time on App'],fd['Yearly Amount Spent'])
sn.jointplot(fd['Time on App'],fd['Yearly Amount Spent'],kind='hex')

data.info()

"""**Plot all the numerical attributes(Avg Session Length, Time on App, Time on Website, Length of Membership and Yearly Amount Spent)**

"""

import seaborn as sns

"""**Avg Session Length vs Yearly Amount Spent**

"""

sns.jointplot(data['Avg Session Length'],data['Yearly Amount Spent'])

"""**Time on App vs Yearly Amount Spent**

"""

sns.jointplot(data['Time on App'],data['Yearly Amount Spent'])

"""**Time on Website vs Yearly Amount Spent**

"""

sns.jointplot(data['Time on Website' ],data['Yearly Amount Spent'])

"""**Length of Membership vs Yearly Amount Spent**

"""

sns.jointplot(data['Length of Membership'],data['Yearly Amount Spent'])

sns.lmplot(x='Yearly Amount Spent',y ='Length of Membership', data=data)

X = data[['Avg Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y = data['Yearly Amount Spent']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=125)

from sklearn.linear_model import LinearRegression

linear = LinearRegression()

linear.fit(X_train,y_train)

print('Coefficients: ', linear.coef_)



predictions = linear.predict(X_test)

plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
print('Mean Squared Error:', mean_squared_error(y_test, predictions))
print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, predictions)))
print('R^2 Score: ',r2_score(y_test, predictions))
