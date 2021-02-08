for _ in range(int(input())):
	string=list(map(str,input().strip()))
	count=0
	
	for i in range(len(string)):
		if count%2==0:

			if string[i]!='a':
				string[i]="a"
			else:
				string[i]="b"
		else:
			if string[i]!="z":
				string[i]="z"
			else:
				string[i]="y"
		count+=1
	print("".join(map(str,string)))
