import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression().fit(x, y)

print('intercept:', model.intercept_)
print('slope', model.coef_)

x_new = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y_new = model.predict(x_new)

print(y_new)