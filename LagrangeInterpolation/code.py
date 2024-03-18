def lagrange(x, y, x0):
    n = len(x)
    y0 = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (x0 - x[j]) / (x[i] - x[j])
        y0 += p * y[i]
    return y0


def main():
    x = [int(i) for i in input("Enter x values: ").split()]
    y = [int(i) for i in input("Enter y values: ").split()]
    x0 = int(input("Enter x0: "))
    
    print("Value of y at x0 is: ", lagrange(x, y, x0))
    
if __name__ == "__main__":
    main()