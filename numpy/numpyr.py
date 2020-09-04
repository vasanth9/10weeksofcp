#shape of array
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) 
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape) 

"""
(2, 4)
[[[[[1 2 3 4]]]]]
shape of array : (1, 1, 1, 1, 4)
"""

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) #4 arrays with 3 indices 1D to 2D

print(newarr,"p") 

newarr = arr.reshape(2, 3, 2)

print(newarr,"t")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base) #view

newarr = arr.reshape(2, 2, -1) #-1 to unknown

print(newarr,"r") 
#flattenn
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr) 
"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]] p
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]] t
[1 2 3 4 5 6 7 8]
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]] r
[1 2 3 4 5 6]
"""
#iterating
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\niterating\n")
for x in arr:
  print(x) 

for x in arr:
    for y in x:
        print(y)
#each scalr nditer()
print("nditer")
for x in np.nditer(arr):
    print(x)
print("iter with step")
for x in np.nditer(arr[:, ::2]):
  print(x) 
print("enumerate")
for idx, x in np.ndenumerate(arr):
  print(idx, x) 

"""

iterating

[1 2 3]
[4 5 6]
1
2
3
4
5
6
nditer
1
2
3
4
5
6
iter with step
1
3
4
6
enumerate
(0, 0) 1
(0, 1) 2
(0, 2) 3
(1, 0) 4
(1, 1) 5
(1, 2) 6
"""
#joining
print("joining")
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr) 

#2d
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
#stacking
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr) 
#hstack
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr) 
#vstack
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr) 

#dstack
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr) 

"""
joining
[1 2 3 4 5 6]
[[1 2 5 6]
 [3 4 7 8]]
[[1 4]
 [2 5]
 [3 6]]
[1 2 3 4 5 6]
[[1 2 3]
 [4 5 6]]
[[[1 4]
  [2 5]
  [3 6]]]
"""
#spliting
print("splitting")
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr) 
#adjusts if less elements
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr) 

print(newarr[0])
#2D splitting
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr) 

#we also have hsplit() ,vsplit() ,dsplit()
"""
splitting
[array([1, 2]), array([3, 4]), array([5, 6])]
[array([1, 2]), array([3, 4]), array([5]), array([6])]
[1 2]
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]]), array([[ 9, 10],
       [11, 12]])]
"""