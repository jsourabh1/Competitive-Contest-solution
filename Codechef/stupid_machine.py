for _ in range(int(input())):

	n=int(input())
	arr=list(map(int,input().split()))

	count=arr[0]
	minn=arr[0]
	for i in range(1,n):
		minn=min(minn,arr[i])
		print(minn,count)
		
		count+=minn
		
	print(count)



