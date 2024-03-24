import math

def f(x):    
    return 1/(1+x**2)

def simpson13(a, b, n):
    h = (b-a)/n
    sum = f(a) + f(b)
    for i in range(1, n):
        if i%2 == 0:
            sum += 2*f(a+i*h)
        else:
            sum += 4*f(a+i*h)
    return sum*h/3

a = 0
b = 1
n = 10

print(simpson13(a, b, n))