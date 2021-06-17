n=int(input())
arr=list(map(int,input().split()))


count=0
s=set()

for i in range(n):

	if arr[i]==1 and i not in s:


		index2=-1
		index1=-1


		#right
		if i!=(n-1):
			for j in range(i+1,n):

				if arr[j]==0:
					index1=j
					break

		#left

		if i!=0:
			for j in range(i-1,-1,-1):

				if arr[j]==0:
					index2=j
					break
		
		if index2==-1 and index1==-1:
			pass


		elif index1==-1:

			count+=abs(i-index2)
			
			arr[index2]=1
			s.add(index2)

		elif index2==-1:

			count+=abs(i-index1)
			
			arr[index1]=1
			s.add(index1)
		else:

			diff1=abs(i-index1)
			diff2=abs(i-index2)

			if diff2<diff1:
				count+=abs(i-index2)
				
				arr[index2]=1
				s.add(index2)
			else:
				count+=abs(i-index1)
				
				arr[index1]=1
				s.add(index1)
		
	
print(count)




