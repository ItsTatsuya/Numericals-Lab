from NewtonBackward import newton_backward_interpolation
from NewtonForward import newton_forward_interpolation

def main(): #
    x = [float(i) for i in input("Enter x values: ").split()]
    y = [float(i) for i in input("Enter y values: ").split()]
    
    value = float(input("Enter value to interpolate: "))
    
    if value < x[len(x)//2]:
        result = newton_forward_interpolation(x, y, value)
        print(f"Interpolated value at {value} is {result} | Forward Interpolation")
    else:
        result = newton_backward_interpolation(x, y, value)
        print(f"Interpolated value at {value} is {result} | Backward Interpolation")
    
if __name__ == "__main__":
    main()