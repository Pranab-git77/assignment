import numpy as np

a = np.array([1, 2, 3, 4])

# dtype is used to check the datatype
print("Original datatype:")
print(a.dtype)

# astype() is used to convert datatype
b = a.astype(float)

print("\nDatatype after conversion:")
print(b.dtype)

print("\nConverted array:")
print(b)