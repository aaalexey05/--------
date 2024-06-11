import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(f"Original array {arr}")
print(f"Array multiplied by 2: {arr * 2}")

print(f"Arrau squared: {arr ** 2}")
print(f"Array sine values: {np.sin(arr)}")

arr2d = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

subArr = arr2d[:2, 1:]
print(f"Original 2D array:\n {arr2d}")
print(f"Subarray:\n {subArr}")