#Introduction to Numpy
##Creating numpy-array
import numpy as np

arr= np.array([1,2,3,4,5])
print(arr)
print(type(arr))

arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2)

arr3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr3)

##Slicing
arr4 = np.array([1,2,3,4])
#[5,6,7,8],[9,10,11,12]])
print(arr4[0:3])
print(arr4[0:])
print(arr4[3:])
print(arr4[:3])

arr5 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr5[0:2,0:2])
print(arr5[0,1:3])
print(arr5[1,1:3])

arr6 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr6[2,2])

##Attribute
arr7 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(np.shape(arr7))
print(np.size(arr7))
print(np.ndim(arr7))
print(arr7.dtype)

##Inspecting an array-Functions
