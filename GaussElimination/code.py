# gauss elimination method  

import numpy as np

def gaussElimination(A, b):
    n = len(b)
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j, i]/A[i, i]
            for k in range(i, n):
                A[j, k] -= factor*A[i, k]
            b[j] -= factor*b[i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += A[i, j]*x[j]
        x[i] = (b[i] - s)/A[i, i]
    return x

def main():
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)
    x = gaussElimination(A, b)
    print(x)
    
if __name__ == "__main__":
    main()