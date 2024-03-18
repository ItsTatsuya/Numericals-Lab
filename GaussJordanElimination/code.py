# gauss jordan elimination method

import numpy as np

def gaussJordanElimination(A, b):
    n = len(b)
    for i in range(n):
        for j in range(n):
            if i != j:
                factor = A[j, i]/A[i, i]
                for k in range(n):
                    A[j, k] -= factor*A[i, k]
                b[j] -= factor*b[i]
    x = np.zeros(n)
    for i in range(n):
        x[i] = b[i]/A[i, i]
    return x

def main():
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)
    x = gaussJordanElimination(A, b)
    print(x)
    
if __name__ == "__main__":
    main()