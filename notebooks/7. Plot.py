import matplotlib.pyplot as plt
import numpy as np

X = [ # 2:(7,2)
    [1, 2],
    [3, 5],
    [6, 2],
    [7, 4],
    [9, 5],
    [10, 3],
    [12, 6],
]

y = [1, 4, 4, 5, 7, 7, 10] # 1:(7,)

n = len(X)

x1 = [X[i][0] for i in range(n)]
x2 = [X[i][1] for i in range(n)]

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(X, y)

print("coef", reg.coef_)
print("intercept", reg.intercept_)
# R^2 es la validación de las regresiones lineales (0 no lineal, 1 lineal completa)
print("r2", reg.score(X, y)) # R^2 (si es cercano a 1, hay un excelente ajuste)

m1 = reg.coef_[0] # primera
m2 = reg.coef_[1] # segunda

b = reg.intercept_

y_predict_1 = [m1 * x1[i] + b for i in range(n)]
y_predict_2 = [m2 * x2[i] + b for i in range(n)]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(0, 12, 25)
Y = np.linspace(0, 8, 25)

# Mezcla dos ejes en una matriz
# X [1, 2, 3]
# Y [4, 5, 6]
# X_ [
#   [1, 4], [1, 5], [1, 6],
#   [2, 4], [2, 5], [2, 6],
#   [3, 4], [3, 5], [3, 6],
# ]
# Y_ [
#   [1, 4], [2, 4], [3, 4],
#   [1, 5], [2, 5], [3, 5],
#   [1, 6], [2, 6], [3, 6],
# ]
X, Y = np.meshgrid(X, Y)

Z = np.zeros((25, 25))

# y(x1, x2) = m1 * x1 + m2 * x2 + b
# Z(X, Y) = m1 * X + m2 * Y + b

# for i in range(25):
#     for j in range(25):
#         Z[i][j] = m1 * X[i][j] + m2 * Y[i][j] + b

Z = m1 * X + m2 * Y + b

ax.plot_surface(X, Y, Z)

ax.scatter(x1, x2, y, c="magenta")

plt.show()