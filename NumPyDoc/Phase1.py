import numpy as np
# print(np._version_)

# //creating array sing list
l=[1,2,3]
arr=np.array(l)
# print(type(arr))
print("hello world")

'''
import time
start=time.time()
l1=[i*2 for i in range(10000)]
print("list", time.time()-start)

start=time.time()
arr1=(np.arange(10000))*2
print("array", time.time()-start)
'''

'''l1=np.zeros((3,5))
l2=np.ones((3,5))
l3=np.full((3,5),0)
print(l1)
print(l2)
print(l3)'''


'''n1=np.array([1.3,2.2,3.8])
n2=n1.astype(int, copy=False)
print(n1)
print(n2)'''


'''n1=np.arange(12)
print(n1)
print(n1.reshape(2,5))   #valueError
print(n1.reshape(3,4))   #possible '''

n1=np.arange(12)
print("original", n1)
print("reshaped", n1.reshape(3,4))
ravelled=n1.ravel()
print("raveled",ravelled)
print("original", n1)