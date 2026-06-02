import numpy as np

a = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print("First row:")
print(a[0])

print("Second column:")
print(a[:, 1])

print("Element 50:")
print(a[1, 1])