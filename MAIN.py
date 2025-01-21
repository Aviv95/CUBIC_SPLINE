from CUBIC_SPLINE import Cubic_Spline

def main():
    print("Hello World!")
    table= [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]
    x=2.5

    print("\nCubic Spline Interpolation:")
    y=Cubic_Spline(table,x)
    print( "\nInterpolated value at x =", x, "is y =", y)

if __name__ == "__main__":
    main()

