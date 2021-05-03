arr=[]


i=1

while i*i<1000000000:
	
	m=i*i
	arr.append(m*2)
	arr.append(m*4)
	i+=1


def solve():

	global arr

	n=int(input())

	if n%2!=0:
		print("No")
		return 

	

	if n in arr:
		print("Yes")
		return 

	print("NO")
	return 


 

t = int(input())
#t = 1


for tt in range(1,t + 1):
    solve()