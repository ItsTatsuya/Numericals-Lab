# gauss sidel method

import numpy as np

def gaussSidel(A, b, x0, tol, maxIter):
    n = len(b)
    x = np.zeros(n)
    for k in range(maxIter):
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i, j]*x[j]
            x[i] = (b[i] - s)/A[i, i]
        if np.linalg.norm(x - x0) < tol:
            return x
        x0 = np.copy(x)
    return x

def main():
    A = np.array([[10, -1, 2],
                  1, 10, -1,
                  2, -1, 10], dtype=float)
    b = np.array([6, 9, 6], dtype=float)
    x0 = np.array([0, 0, 0], dtype=float)
    tol = 1e-10
    maxIter = 100
    x = gaussSidel(A, b, x0, tol, maxIter)
    print(x)
    
if __name__ == "__main__":
    main()