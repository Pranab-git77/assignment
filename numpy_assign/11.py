import numpy as np

a=np.array([1])

#this will give a error because a is 1D array and we are trying to access 2D array
print(a[:,1])