import numpy as np

def describe_array(arr):
    return(f"the dimensions of the array are: {arr.ndim}\nthe shape of array is:{arr.shape}\nthe size of array is:{arr.size}\nthe dype of array is:{arr.dtype}")


a_1d= np.array([1,2,3,4,5])
print(describe_array(a_1d))

a_2d= np.array([[1,2,3],[5,6,7]])
print(describe_array(a_2d))

a_3d=np.array([])
print(describe_array(a_3d))