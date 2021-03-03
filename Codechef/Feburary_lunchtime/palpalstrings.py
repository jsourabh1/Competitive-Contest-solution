
#second qeustion
	#question link:-https://www.codechef.com/LTIME93B/problems/PALPALS
	# the qeustion is want  :-
	# first you have to divided in many continous substring string which are palindrom 
	# and tell yes/no whether you arrange orignal string in this sense
	#observation:-
	#the basic thing is that for the palindrome string all the charactar repleated 
	#more than 2 times except the middle one element eg:- aba,aaabaaa
	#so basically you have to count the frequecy of all the charactars
	#and check that the charactars whose frquecy is one is greater or smaller then 
	# then whose frequecy greater then 1
	#if greater then print(no)
	#else print(yes) 
	#solution id:-https://www.codechef.com/viewsolution/43322825
from collections import Counter
def solve(string):
	one=other=0
	dict1=Counter(string)
	for i in dict1.values():
		if i==1:
			one+=1
		elif i%2==0:
			other+=i//2
		else:
			other+=(i-3)//2

	if other>=one:
		print("YES")
	else:
		print("NO")
	return 
for i in range(int(input())):
	string=str(input())
	solve(string)
