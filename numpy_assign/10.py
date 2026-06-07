import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8]])

print("shape of a:",a.shape)
print("number of dimensions:",a.ndim)
print("size of a:",a.size)
print("data type of a:",a.dtype)
n=a.astype(bool)
print("data type of n:",n.dtype)