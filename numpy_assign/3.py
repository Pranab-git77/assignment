import numpy as np

a = np.arange(1, 13)

print("(3,4)")
print(a.reshape(3,4))

print("\n(2,6)")
print(a.reshape(2,6))

print("\n(2,3,2)")
print(a.reshape(2,3,2))