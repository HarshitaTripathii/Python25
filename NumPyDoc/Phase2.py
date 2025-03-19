import numpy as np

'''l=[1,2,3,4,5,6,7]
print(l[1:5])'''

'''l1=np.array([11,22,33,44,55,66,77,88,99])
n2=l1.reshape(3,3)
# print(n2)
print("1 element ", n2[1,1])
print("1 row ", n2[2])
print("1 column ", n2[:, 2]) '''

'''# SORTING
n=np.array([2,4,9,1,0,2,44,6])
n1=n.reshape(4,2)
print("original ")
print(n1)
ns0=np.sort(n1, axis=0)
print("top to bottom")
print(ns0)
ns1=np.sort(n1, axis=1)
print("left to right")
print(ns1)'''

'''# FANCY INDEXING IN NUMPY
n1=np.arange(1,11)
print(n1)
n2=n1[n1%2==0]
print(n2)

n3=n1[n1>5]
print(n3)'''

'''#  filter using mask
# n1=np.arange(1,11)
l1=[11,34,0,23,5,6,2,1,88,2]
n1=np.array(l1)
msk=n1>5
print(msk)
n2=n1[msk]
print(n2)'''

'''
#  array additiion
n1=np.array([1,2,3])
n2=np.array([4,5,3])
n3=np.concatenate((n1,n2))
print(n3)'''

#  adding new row : vertical stack : vstack : np.vstack((original array, new row))
#  adding new column : horizontal stack : hstack : np.hstack((original array, new column))

'''n1=np.array([1,2,3,4])
n2=n1.reshape(2,2)
# print(n2)

new_row=np.array([5,6])
n22=np.vstack((n2, new_row))
print(n22)

new_col=np.array([[22], [44],[66]])
n222=np.hstack((n22, new_col))
print(n222)'''