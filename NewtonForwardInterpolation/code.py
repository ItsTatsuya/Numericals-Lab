# newton forward interpolation method

import numpy as np

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def newton_forward_interpolation(x, y, n, value):
    h = x[1] - x[0]
    u = (value - x[0]) / h
    sum = y[0]
    for i in range(1, n):
        temp = 1
        for j in range(i):
            temp *= (u - j)
        temp = temp / fact(i)
        sum += temp * y[i]
    return sum

def main():
    x = np.array([1891, 1901, 1911, 1921, 1931])
    y = np.array([46, 66, 81, 93, 101])
    n = len(x)
    value = 1925
    solution = newton_forward_interpolation(x, y, n, value)
    print("The value at", value, "is", solution)
    
if __name__ == "__main__":
    main()
    