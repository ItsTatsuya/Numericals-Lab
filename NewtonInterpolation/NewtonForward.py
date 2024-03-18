def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def newton_forward_interpolation(x, y, value):
    n = len(x)
    h = x[1] - x[0]
    u = (value - x[0]) / h
    y0 = y[0]
    y_diff = [[0 for i in range(n)] for j in range(n)]
    y_diff[0] = y
    for i in range(1, n):
        for j in range(n-i):
            y_diff[i][j] = y_diff[i-1][j+1] - y_diff[i-1][j]
    result = y0
    for i in range(1, n):
        product = 1
        for j in range(i):
            product *= (u - j)
        result += product * y_diff[i][0] / fact(i)
    return result
