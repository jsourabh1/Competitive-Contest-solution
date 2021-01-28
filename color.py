from collections import Counter
for _ in range(int(input())):

	n=int(input())
	arr=list(map(int,input().split()))

	arr_1=Counter(arr)
	print(max(arr_1.values()))