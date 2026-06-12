import numpy as np

a = np.array([
    [11,22,33],
    [44,55,66],
    [77,88,99]
])

print("First column:")
print(a[:, 0])

print("Last row:")
print(a[-1])

print("Required output:")
print(a[:2, 1:])

print(a[0:2,0:2])