#third qustion 
	#question link:-https://www.codechef.com/LTIME93B/problems/AVGSORT
	# in this question we have to make the array striclty increasing 
	#solution id:-https://www.codechef.com/viewsolution/43322969
def solve():
	n=int(input())
	arr=list(map(int,input().split()))
	isdecreasing=True
	for i in range(len(arr)-1):
		if arr[i]<arr[i+1]:
			isdecreasing=False
	if isdecreasing:
		print("NO")
	else:
		print("YES")
for i in range(int(input())):
	solve()