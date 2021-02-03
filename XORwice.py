from math import pow
for _ in range(int(input())):

	n,m=map(int,input().split())
	num1=n&m

	print((n^num1)+m^num1)