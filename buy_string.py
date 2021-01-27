for _ in range(int(input())):

	n,c,d,e=map(int,input().split())
	string=list(map(str,input().strip()))
	count_1=0
	
	for i in string:
		if i=="0":
			count_1+=c
		else:
			count_1+=d
	

	
	if c>d:
		count_2=0

		for i in range(len(string)):
			if string[i]=="0":
				string[i]="1"
				count_2+=e

		for i in string:
			if i=='0':
				count_2+=c
			else:
				count_2+=d
	else:
		count_2=0

		for i in range(len(string)):
			if string[i]=="1":
				string[i]="0"
				count_2+=e

		print

		for i in string:
			if i=='0':
				count_2+=c
			else:
				count_2+=d

	print(min(count_1,count_2))

