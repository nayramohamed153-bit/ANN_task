import numpy as np

# -------- Activation Function --------
def tanh(x):
    return np.tanh(x)

np.random.seed(42)  

W1 = np.random.uniform(-0.5, 0.5, (2, 2))


W2 = np.random.uniform(-0.5, 0.5, (2, 2))


b1 = 0.5   # hidden layer bias
b2 = 0.7   # output layer bias


X = np.array([[0.05, 0.10]])


Z1 = np.dot(X, W1) + b1
A1 = tanh(Z1)


Z2 = np.dot(A1, W2) + b2
A2 = tanh(Z2)


print("Input:")
print(X)

print("\nWeights Input -> Hidden:")
print(W1)

print("\nWeights Hidden -> Output:")
print(W2)

print("\nHidden Layer Output:")
print(A1)

print("\nFinal Network Output:")
print(A2) 