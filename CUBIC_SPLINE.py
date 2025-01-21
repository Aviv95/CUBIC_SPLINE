import numpy as np

def Cubic_Spline(table, x):
    """
    Performs cubic spline interpolation at a given point `x` using the data from `table`.
    :param table: A list of tuples [(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)] of known data points.
    :param x: The value at which we want to compute the interpolated y-value.
    :return: The interpolated y-value at x.
    """
    # Extract x and y values from the table
    X = [t[0] for t in table]
    Y = [t[1] for t in table]

    # Number of data points
    n = len(table)

    h = [X[i + 1] - X[i] for i in range(n-1)]

    # We'll calculate the second derivatives (c) of the spline using the tridiagonal system
    A = np.zeros((n, n))  # Coefficient matrix
    b = np.zeros(n)  # Right-hand side vector

    # Print the Natural Spline Table from 1 to 6
    print(f"\n{'Natural Spline Table':^50}")
    print(f"{'Iteration':<10} | {'X':<15} | {'Y':<15} | {'c':<15} | {'Result':<15}")
    print("-" * 94)

    # Set up the system for internal points
    for i in range(n-1):  # loop from 0 to n-1 to include all 6 points
        A[i][i] = 2 * (h[i-1] + h[i]) if i > 0 else 2 * h[i]
        A[i][i+1] = h[i] if i < n-2 else 0
        A[i][i-1] = h[i-1] if i > 0 else 0
        b[i] = 3 * ((Y[i + 1] - Y[i]) / h[i] - (Y[i] - Y[i - 1]) / h[i - 1]) if i > 0 else 0
        # print for iteration
        print(f"{i+1:<10} | {X[i]:<15} | {Y[i]:<15} | {b[i]:<15.6f} | [{A[i][i-1]:<.4f} , [{A[i][i]:<.4f} , {A[i][i+1]:<.4f}]")
        print("-" * 94)

    # Set the boundary conditions (natural spline)
    A[0][0] = 1
    A[-1][-1] = 1
    b[0] = 0
    b[-1] = 0

    # Solve the system of equations to find the second derivatives (c)
    c = np.linalg.solve(A, b)

    # Full Spline Calculation Table from 1 to 6
    print(f"\n{'Full Spline Table':^50}")
    print(f"{'Iteration':<10} | {'c':<10} | {'a':<10} | {'b':<10} | {'d':<10} | {'y_interpolated':<10}")
    print("-" * 80)

    # Step 3: Calculate the coefficients a, b, c, d for each spline segment
    a = Y[:-1]
    b_coeff = [(Y[i + 1] - Y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3 for i in range(n - 1)]
    d = [(c[i + 1] - c[i]) / (3 * h[i]) for i in range(n - 1)]

    # Step 4: Find the segment where the point `x` lies
    for i in range(n - 1):
         # Print the coefficient values for each segment
         print(f"{i:<10} | {c[i]:<10.6f} | {a[i]:<10.6f} | {b_coeff[i]:<10.6f} | {d[i]:<10.6f}", end=" | ")
         # Compute the interpolated value at `x` if x is between X[i] and X[i + 1]
         if X[i] <= x <= X[i + 1]:
             dx = x - X[i]
             y_interpolated = a[i] + b_coeff[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3
             print(f"{y_interpolated:<10.6f}")  # Print the interpolated value for this segment
             print("-" * 80)
             return y_interpolated
         else:
             print("N/A")  # If x is not in this segment, mark it as N/A

    # If x is out of bounds, return None (or raise an error, depending on your needs)
    return None