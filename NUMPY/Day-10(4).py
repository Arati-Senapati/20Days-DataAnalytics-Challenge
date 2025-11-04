import numpy as np

#sort an array
arr = np.array([[7,8,4,12,9],[2,8,5,1,3]])
print(np.sort(arr))

#search
arr = np.array([3,4,2,7,8])
s = np.where(arr % 2 == 0)
print(s)

#searchsorted
arr = np.array([1,2,3,4,5])
ss = np.searchsorted(arr,4)
print(ss)

#filter
arr = np.array([20,30,40,50])
fa = [True,False,True,False]

new =arr[fa]
print(new)

arr = np.array([20,30,40,50])
fa = arr>35
new = arr[fa]
print(new)