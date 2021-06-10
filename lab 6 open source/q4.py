import numpy as np


matrix = np.array([[5, 4],[6, 3]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(eigenvalues)
print(eigenvectors)