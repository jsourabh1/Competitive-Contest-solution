import time 


def solve(arr,n,k):


	ans=0
	while k:
		stop=0
		for i in range(0,n-1):
			if arr[i]<arr[i+1]:
				stop=1
				ans=i+1
				arr[i]+=1
				break

		k-=1
	if stop==0:
		print(-1)
	else:
		print(ans)
	return 


for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	solve(arr,n,k)
