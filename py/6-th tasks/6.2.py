import numpy as np
n = 10
a = np.zeros((n, n))
a[0, 0] = 2
a[0, 1] = -1
a[-1, -1] = 2
a[-1, -2] = -1
for i in range(1, n-1):
    a[i, i] = 2
    a[i, i-1] = -1
    a[i, i+1] = -1
eigenvalues, eigenvectors = np.linalg.eigh(a)

print(eigenvalues[0])
print(eigenvectors[:,0])
