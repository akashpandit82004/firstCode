# num=5
# fact=1
# while num>0:
#     fact=fact*num
#     num=num-1
#     print(fact)
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])   # relationship y = 2x

# Parameters
m = 0   # slope
c = 0   # intercept
alpha = 0.01  # learning rate
epochs = 1000

n = len(X)

# Batch Gradient Descent
for _ in range(epochs):
    y_pred = m * X + c
    D_m = (-2/n) * sum(X * (y - y_pred).flatten())
    D_c = (-2/n) * sum(y - y_pred.flatten())
    m = m - alpha * D_m
    c = c - alpha * D_c

print("Final Model: y =", round(m, 2), "x +", round(c, 2))
