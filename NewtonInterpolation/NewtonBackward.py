def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def newton_backward_interpolation(x, y, value):
    n = len(x)
    h = x[1] - x[0]
    u = (value - x[n-1]) / h
    y0 = y[n-1]
    y_diff = [[0 for i in range(n)] for j in range(n)]
    y_diff[0] = y
    for i in range(1, n):
        for j in range(n-i):
            y_diff[i][j] = y_diff[i-1][j] - y_diff[i-1][j+1]
    result = y0
    for i in range(1, n):
        result += (u-i+1) * y_diff[i][n-i-1] / fact(i)
    return result

