#false position method
import math

def bisect(f, a, b, absolute_error):
    if f(a) * f(b) > 0: 
        return None
    while (b - a) / 2 > absolute_error:
        c = (a*f(b) - b*f(a))/(f(b)-f(a))
        if abs(f(c)) < absolute_error:
            return c
        elif f(b) * f(c) < 0:
            a, b = c, b
        else:
            a, b = a, c

    return (a + b) / 2
function = input("Enter function: ")
f = lambda x: eval(function)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

absolute_error = float(input("Enter absolute error: "))

root = bisect(f, a, b, absolute_error)
if root is None:
    print("\nRoot not found. Try again with different values.")
else:
    print("\nRoot: ", root)
    print("f(root): ", f(root))


