# newton Raphson method

import numpy as np

def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

def newtonRaphson(x0, tol, maxIter):
    for i in range(maxIter):
        x = x0 - f(x0)/df(x0)
        if abs(x - x0) < tol:
            return x
        x0 = x
    return x

def main():
    x0 = 3
    tol = 1e-10
    maxIter = 100
    x = newtonRaphson(x0, tol, maxIter)
    print(x)
    
if __name__ == "__main__":
    main()
    