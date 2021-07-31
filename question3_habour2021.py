#DaRk DeveLopeR


'''
C. Penalty
time limit per test3 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Consider a simplified penalty phase at the end of a football match.

A penalty phase consists of at most 10 kicks, the first team takes the first kick, the second team takes the second kick, then the first team takes the third kick, and so on. The team that scores more goals wins; if both teams score the same number of goals, the game results in a tie (note that it goes against the usual football rules). The penalty phase is stopped if one team has scored more goals than the other team could reach with all of its remaining kicks. For example, if after the 7-th kick the first team has scored 1 goal, and the second team has scored 3 goals, the penalty phase ends — the first team cannot reach 3 goals.

You know which player will be taking each kick, so you have your predictions for each of the 10 kicks. These predictions are represented by a string s consisting of 10 characters. Each character can either be 1, 0, or ?. This string represents your predictions in the following way:

if si is 1, then the i-th kick will definitely score a goal;
if si is 0, then the i-th kick definitely won't score a goal;
if si is ?, then the i-th kick could go either way.
Based on your predictions, you have to calculate the minimum possible number of kicks there can be in the penalty phase (that means, the earliest moment when the penalty phase is stopped, considering all possible ways it could go). Note that the referee doesn't take into account any predictions when deciding to stop the penalty phase — you may know that some kick will/won't be scored, but the referee doesn't.

Input
The first line contains one integer t (1≤t≤1000) — the number of test cases.

Each test case is represented by one line containing the string s, consisting of exactly 10 characters. Each character is either 1, 0, or ?.

Output
For each test case, print one integer — the minimum possible number of kicks in the penalty phase.

Example
inputCopy
4
1?0???1001
1111111111
??????????
0100000000
outputCopy
7
10
6
9
Note
Consider the example test:

In the first test case, consider the situation when the 1-st, 5-th and 7-th kicks score goals, and kicks 2, 3, 4 and 6 are unsuccessful. Then the current number of goals for the first team is 3, for the second team is 0, and the referee sees that the second team can score at most 2 goals in the remaining kicks. So the penalty phase can be stopped after the 7-th kick.

In the second test case, the penalty phase won't be stopped until all 10 kicks are finished.

In the third test case, if the first team doesn't score any of its three first kicks and the second team scores all of its three first kicks, then after the 6-th kick, the first team has scored 0 goals and the second team has scored 3 goals, and the referee sees that the first team can score at most 2 goals in the remaining kicks. So, the penalty phase can be stopped after the 6-th kick.

In the fourth test case, even though you can predict the whole penalty phase, the referee understands that the phase should be ended only after the 9-th kick.


question link:- https://codeforces.com/contest/1553/problem/C
'''
import sys


#taking input as string 
input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda: list(map(int,sys.stdin.readline().rstrip("\r\n").split()))
mod = 10**9+7; Mod = 998244353; INF = float('inf')
#______________________________________________________________________________________________________
import math
from bisect import *
from heapq import *
from collections import defaultdict as dd
from collections import OrderedDict as odict
from collections import Counter as cc
from collections import deque
from itertools import groupby
sys.setrecursionlimit(20*20*20*20+10) #this is must for dfs

def help(s):
	n=len(s)//2
	aw=0
	al=n
	bw=0
	bl=n
	count=0
	
	for i in range(0,2*n):
		count+=1
		if(count==(2*n)):
		    break
		if(i%2==0):
			if(s[i]=='1'):
				aw+=1
			else:
				al-=1
			if(aw>bl):
				# print(count)
				return count
				break
			if(al<bw):
				# print(count)
				return count
				break
		else:
			if(s[i]=='1'):
				bw+=1
			else:
				bl-=1
			if(bw>al):
				# print(count)
				return count
				break
			if(bl<aw):
				# print(count)
				return count
				break
	if(count==(2*n)):
		return count

def solve():

	string=list(map(str,input().strip()))
	n=len(string)
	c=string.copy()


	for i in range(0,n,2):

		if string[i]=='?':
			string[i]='1'


	first=help(string)


	string=c.copy()
	for i in range(1,n,2):

		if string[i]=="?":
			string[i]='1'

	

	second=help(string)

	print(min(first,second))


def main():
    global tt
    if not ONLINE_JUDGE:
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    t = 1
    t = takein()
    #t = 1
    for tt in range(1,t + 1):
        solve()
    if not ONLINE_JUDGE:
        print("Time Elapsed :",time.time() - start_time,"seconds")
        sys.stdout.close()

#---------------------- USER DEFINED INPUT FUNCTIONS ----------------------#
def takein():
    return (int(sys.stdin.readline().rstrip("\r\n")))


# input the string

def takesr():
    return (sys.stdin.readline().rstrip("\r\n"))


# input int array
def takeiar():
    return (list(map(int, sys.stdin.readline().rstrip("\r\n").split())))


# input string array
def takesar():
    return (list(map(str, sys.stdin.readline().rstrip("\r\n").split())))


# innut values for the diffrent variables
def takeivr():
    return (map(int, sys.stdin.readline().rstrip("\r\n").split()))


def takesvr():
    return (map(str, sys.stdin.readline().rstrip("\r\n").split()))

 
 
#------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#



def ispalindrome(s):

	return s==s[::-1]
 
def invert(bit_s):


	  
	# convert binary string 
	# into integer
	temp = int(bit_s, 2)
	  
	# applying Ex-or operator
	# b/w 10 and 31
	inverse_s = temp ^ (2 ** (len(bit_s) + 1) - 1)
	  
	# convert the integer result 
	# into binary result and then 
	# slicing of the '0b1' 
	# binary indicator
	rslt = bin(inverse_s)[3 : ]

	return str(rslt) 	  

def counter(a):
    q = [0] * max(a)
    for i in range(len(a)):
        q[a[i] - 1] = q[a[i] - 1] + 1
    return(q)
 
def counter_elements(a):
    q = dict()
    for i in range(len(a)):
        if a[i] not in q:
            q[a[i]] = 0
        q[a[i]] = q[a[i]] + 1
    return(q)
 
def string_counter(a):
    q = [0] * 26
    for i in range(len(a)):
        q[ord(a[i]) - 97] = q[ord(a[i]) - 97] + 1
    return(q)
 
def factorial(n,m = 1000000007):
    q = 1
    for i in range(n):
        q = (q * (i + 1)) % m
    return(q)
 
def factors(n):
    q = []
    for i in range(1,int(n ** 0.5) + 1):
        if n % i == 0: q.append(i); q.append(n // i)
    return(list(sorted(list(set(q)))))
 
def prime_factors(n):
    q = []
    while n % 2 == 0: q.append(2); n = n // 2
    for i in range(3,int(n ** 0.5) + 1,2):
        while n % i == 0: q.append(i); n = n // i
    if n > 2: q.append(n)
    return(list(sorted(q)))
 
def transpose(a):
    n,m = len(a),len(a[0])
    b = [[0] * n for i in range(m)]
    for i in range(m): 
        for j in range(n): 
            b[i][j] = a[j][i]
    return(b)
 
def power_two(x):
    return (x and (not(x & (x - 1))))
 
def ceil(a, b):
    return -(-a // b)



def seive(n):
	a = [1]
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
	    if (prime[p] == True): 
	        for i in range(p ** 2,n + 1, p): 
	            prime[i] = False
	    p = p + 1
	for p in range(2,n + 1): 
	    if prime[p]: 
	        a.append(p)
	return(a)

 
def pref(li):
    pref_sum = [0]
    for i in li:
        pref_sum.append(pref_sum[-1]+i)
    return pref_sum
 
def kadane(x):  # maximum sum contiguous subarray
    sum_so_far = 0
    current_sum = 0
    for i in x:
        current_sum += i
        if current_sum < 0:
            current_sum = 0
        else:
            sum_so_far = max(sum_so_far, current_sum)
    return sum_so_far

def binary_search(li, val):
    # print(lb, ub, li)
    ans = -1
    lb = 0
    ub = len(li)-1
    while (lb <= ub):
        mid = (lb+ub) // 2
        # print('mid is',mid, li[mid])
        if li[mid] > val:
            ub = mid-1
        elif val > li[mid]:
            lb = mid+1
        else:
            ans = mid  # return index
            break
    return ans


 
def upper_bound(li, num):
    answer = -1
    start = 0
    end = len(li)-1
 
    while (start <= end):
        middle = (end+start) // 2
 
        if li[middle] <= num:
            answer = middle
            start = middle+1
 
        else:
            end = middle-1
    return answer  # max index where x is not greater than num


def lower_bound(li, num):
    answer = -1
    start = 0
    end = len(li)-1
 
    while (start <= end):
        middle = (end+start) // 2
        if li[middle] >= num:
            answer = middle
            end = middle-1
        else:
            start = middle+1
    return answer  # min index where x is not less than num
#-----------------------------------------------------------------------#
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    input = sys.stdin.readline
    
main()