#false position method
import math

def falseposition(f, a, b, absolute_error):
    iterations = 0
    if f(a) * f(b) > 0: 
        return None, iterations
    while (b - a) / 2 > absolute_error:
        iterations += 1
        c = (a*f(b) - b*f(a))/(f(b)-f(a))
        if abs(f(c)) < absolute_error:
            return c, iterations
        elif f(b) * f(c) < 0:
            a, b = c, b
        else:
            a, b = a, c

    return ((a + b) /  2), iterations

if __name__ == "__main__":
    function = input("Enter function: ")
    f = lambda x: eval(function)
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    absolute_error = float(input("Enter absolute error: "))

    root,itera = falseposition(f, a, b, absolute_error)
    if root is None:
        print("\nRoot not found. Try again with different values.")
    else:
        print("\nRoot: ", root)
        print("Iterations: ", itera)


