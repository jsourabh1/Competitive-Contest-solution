def solve(arr,string,n,m):
	if m==1:
		for _ in range(n):
			print("yes")

	else:
		

		for i in arr:

			if i>=int(string):
				print("yes")

			elif i%m==0:
				print("yes")

			else:
				flag=0
				while True and i>0:

					if str(i).count(str(m))>=1:
						print("yes")
						flag=1
						break
					
					i-=m
					

				if flag==0:
					print("no")



	return 




for i in range(int(input())):

	o,k=map(int,input().split())
	array =list(map(int,input().split()))
	stri_1=str(k)+"0"
	solve(array,stri_1,o,k)


	