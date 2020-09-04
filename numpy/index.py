import numpy as np
print(np.__version__)
arr=np.array([1,2,3,4,5]) #list
print(arr)
print(type(arr))
arr=np.array((1,2,3,4,5)) #tuple
print(arr)
"""
1.19.1
[1 2 3 4 5]
<class 'numpy.ndarray'>
[1 2 3 4 5]
"""
#dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[-1, -2, -3], [-4, -5, -6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim) 
"""
0
1
2
3
"""
#higher dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim) 
#[[[[[1 2 3 4]]]]]
#number of dimensions : 5

#indexing
print("2nd el of 1D:",b[1])
print("3rd of 2nd arr of 2D:",c[1][2]," ",c[1,2])
print("el of 3d:",d[1,1,2])
print("el of 3rd -ve:",d[0,1,-2])
"""
2nd el of 1D: 2
3rd of 2nd arr of 2D: 6   6
el of 3d: -6
el of 3rd -ve: 5
"""

#slicing

#[start:end]
#[start:end:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)
print(arr[1:5]) 
#includes start index and excludes end index
print(arr[3:]) #to end
print(arr[:4]) #from start
print(arr[-3:-1]) #negative
print(arr[1:5:2]) #step 2
print(arr[::2]) #even indices
#2d slices
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1])
print(arr[1, 1:4]) 
print(arr[0:2,2]) #2nd index of arrays
print(arr[:,1:4])
"""
[1 2 3 4 5 6 7]
[2 3 4 5]
[4 5 6 7]
[1 2 3 4]
[5 6]
[2 4]
[1 3 5 7]
[ 6  7  8  9 10]
[7 8 9]
[3 8]
[[2 3 4]
 [7 8 9]]
"""
 #datatypes
"""
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
"""
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype) 

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype) 

arr = np.array([1.1, 2.1, 3.1])
print(arr)
#astype() to change datatype
newarr = arr.astype('i')
print(arr.dtype)
print(newarr)
print(newarr.dtype) 

"""
[b'1' b'2' b'3' b'4']
|S1
[1 2 3 4]
int32
[1.1 2.1 3.1]
float64
[1 2 3]
int32
"""

#view vs copy
#changes doesn't affect other in copy whre in view it does

arr = np.array([1, 2, 3, 4, 5])
y = arr.copy()
arr[0] = 42

print(arr)
print(y) 
x = arr.view()
arr[0] = 42
x[2]=5
print(arr)
print(x) 
#check originality
print(x.base)
print(y.base)
#copy gives None and view gives original array
"""
[42  2  3  4  5]
[1 2 3 4 5]
[42  2  5  4  5]
[42  2  5  4  5]
[42  2  5  4  5]
None
"""