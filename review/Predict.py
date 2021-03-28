x1 = [1, 3, 1, 0]
x2 = [2, 2, 0, 1]
x3 = [3, 1, 1, 1]

import numpy as np

X = np.array([
    x1,
    x2,
    x3,
]).T

y = [1, 2, 3, 4]

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(X, y)

print(reg.score(X, y))

print(reg.coef_)