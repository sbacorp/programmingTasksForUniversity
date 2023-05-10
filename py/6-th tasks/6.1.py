import numpy as np
n = 8
# матрцина
a = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        a[i, j] = (i+j+1) * np.math.factorial(i+j) / (np.math.factorial(i) * np.math.factorial(j) * np.math.factorial(i+j+1))

eigenvalues, eigenvectors = np.linalg.eig(a)
idx = eigenvalues.argsort()[:3]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]
print("Три наименьших собственных значения:")
print(eigenvalues)
print("собственные векторы:")
print(eigenvectors)
