import numpy as np

# Python list can store different data types
list = [80,"Hello",3.5]
print("Python List:")
print(list)

# NumPy array is mainly used for numerical data
array = np.array([10,20,30,40])
print("\nNumPy Array:")
print(array)

# Lists do not perform element-wise addition
l1 = [8,5,6]
l2 = [7,8,4]
print("\nList Addition:")
print(l1+l2)  # Concatenates the lists

# NumPy arrays perform element-wise addition
array1=np.array([1,2,3])
array2=np.array([4,5,6])
print("\nArrayAddition:")
print(array1+array2)