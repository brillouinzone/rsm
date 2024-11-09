import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x, y)
def f(x, y):
    return np.sqrt(x) + np.sqrt(y) - 5 + np.sqrt(x * y) - 5

# Define the range and resolution of the meshgrid
x_vals = np.linspace(0.01, 10, 1010)  # Avoid 0 to prevent sqrt(0) issues
y_vals = np.linspace(0.01, 10, 1010)

# Create the 2D meshgrid
X, Y = np.meshgrid(x_vals, y_vals)

# Compute f(x, y) for all points in the mesh
Z = np.abs(f(X, Y))

# Plot the result as a contour plot
plt.contourf(X, Y, Z, 20, cmap='viridis',vmin=0)
plt.colorbar(label='|f(x, y)|')
plt.xlabel('x')
plt.ylabel('y')
plt.title('The values of x and y that minimize |f(x, y)| are: x = 7.84, y = 3.59')
plt.show()

x_guess=0.263932
y_guess=4.73606797749979
x_guess=np.sqrt(9.7)
y_guess=np.sqrt(2.8)


print(f"guess:{f(np.power(x_guess,2),np.power(y_guess,2))}")
# Find the index of the minimum absolute value of f(x, y)
min_index = np.unravel_index(np.argmin(np.abs(Z)), Z.shape)

# Retrieve the corresponding x and y values
x_min = X[min_index]
y_min = Y[min_index]

# Output the result
print(f"The values of x and y that minimize |f(x, y)| are: x = {x_min}, y = {y_min}")
print(f"f={f(x_min,y_min)}")