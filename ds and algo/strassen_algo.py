import math
def solve2(x,y):
	c=np.zeros((len(x),len(x)))
	for i in range(len(x)):
		for j in range(len(x)):
			c[i][j]=0
			for k in range(len(x)):

				c[i][j]+=x[i][k]*y[k][j]
			print(c)
	print(c)

import numpy as np
def split(a):
	row,colu=a.shape
	row1,colu1=row//2,colu//2

	return a[:row1,:colu1],a[:row1,colu1:],a[row1:,:colu1],a[row1:,colu1:]

def solve(x,y):
	
	if len(x)==1:

		return x*y
	else:
		a,b,c,d=split(x)
		e,f,g,h=split(y)
		print(a,b,c,d,e,f,g,h)
		m1=solve(a+d,e+h)
		m2=solve(c+d,e)
		m3=solve(a,f-h)
		m4=solve(d,g-e)
		m5=solve(a+b,h)
		m6=solve(c-a,e+f)
		m7=solve(d-c,g+h)
		print(m1,m2,m3,m4,m5,m6,m7)

		c11=m1+m4+m7-m5

		c12=m3+m5
		c21=m2+m4
		c22=m1-m2+m3+m6
		print(c11,c12,c21,c22)

		c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

		return c



array1=np.array([[1,2,3],[4,5,6],[7,8,9]])
array2=np.array([[1,2,1],[2,4,6],[7,2,5]])
if len(array1)%2==0:
	print(solve2(array1,array2))
	print(solve(array1,array2))
else:
	#print(solve2(array1,array2))
	
	n=2**math.ceil(math.log(len(array1),2))
	print(n)
	padding1=np.zeros((n,n))
	padding2=np.zeros((n,n))
	print(padding1,padding2)
	padding1[:len(array1),:len(array1)]=array1
	padding2[:len(array1),:len(array1)]=array2
	print(padding1,padding2)
	print(solve(padding1,padding2))


