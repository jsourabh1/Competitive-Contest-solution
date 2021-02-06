
for _ in range(int(input())):

	n,m=map(int,input().split())
	string=input()
	U=string.count("U")
	D=string.count("D")
	L=string.count("L")
	R=string.count("R")
	#print(L,R,U,D)

	if n<=0 and m<=0:
		#print(1)
		if L>=abs(n) and D>=abs(m):
			print("YES")
		else:
			print("NO")
	elif n>=0 and m>=0:
	#	print(2)
		if R>=abs(n) and U>=abs(m):
			print("YES")
		else:
			print("NO")
	elif n>=0 and m<=0:	
	#	print(3)
		if R>=abs(n) and D>=abs(m):
			print("YES")
		else:
			print("NO")
	else:
	#	print(4)
		if L>=abs(n) and U>=abs(m):
			print("YES")
		else:
			print("NO")

