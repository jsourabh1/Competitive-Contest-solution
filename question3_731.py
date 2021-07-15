#DaRk DeveLopeR
'''


Monocarp and Polycarp are learning new programming techniques. Now they decided to try pair programming.

It's known that they have worked together on the same file for n+m minutes. Every minute exactly one of them made one change to the file. Before they started, there were already k lines written in the file.

Every minute exactly one of them does one of two actions: adds a new line to the end of the file or changes one of its lines.

Monocarp worked in total for n minutes and performed the sequence of actions [a1,a2,…,an]. If ai=0, then he adds a new line to the end of the file. If ai>0, then he changes the line with the number ai. Monocarp performed actions strictly in this order: a1, then a2, ..., an.

Polycarp worked in total for m minutes and performed the sequence of actions [b1,b2,…,bm]. If bj=0, then he adds a new line to the end of the file. If bj>0, then he changes the line with the number bj. Polycarp performed actions strictly in this order: b1, then b2, ..., bm.

Restore their common sequence of actions of length n+m such that all actions would be correct — there should be no changes to lines that do not yet exist. Keep in mind that in the common sequence Monocarp's actions should form the subsequence [a1,a2,…,an] and Polycarp's — subsequence [b1,b2,…,bm]. They can replace each other at the computer any number of times.

Let's look at an example. Suppose k=3. Monocarp first changed the line with the number 2 and then added a new line (thus, n=2,a=[2,0]). Polycarp first added a new line and then changed the line with the number 5 (thus, m=2,b=[0,5]).

Since the initial length of the file was 3, in order for Polycarp to change line number 5 two new lines must be added beforehand. Examples of correct sequences of changes, in this case, would be [0,2,0,5] and [2,0,0,5]. Changes [0,0,5,2] (wrong order of actions) and [0,5,2,0] (line 5 cannot be edited yet) are not correct.

Input
The first line contains an integer t (1≤t≤1000). Then t test cases follow. Before each test case, there is an empty line.

Each test case contains three lines. The first line contains three integers k, n, m (0≤k≤100, 1≤n,m≤100) — the initial number of lines in file and lengths of Monocarp's and Polycarp's sequences of changes respectively.

The second line contains n integers a1,a2,…,an (0≤ai≤300).

The third line contains m integers b1,b2,…,bm (0≤bj≤300).

Output
For each test case print any correct common sequence of Monocarp's and Polycarp's actions of length n+m or -1 if such sequence doesn't exist.

Example
inputCopy
5

3 2 2
2 0
0 5

4 3 2
2 0 5
0 6

0 2 2
1 0
2 3

5 4 4
6 0 8 0
0 7 0 9

5 4 1
8 7 8 0
0
outputCopy
2 0 0 5 
0 2 0 6 5 
-1
0 6 0 7 0 8 0 9
-1


question link:-https://codeforces.com/contest/1547/problem/C
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



def solve():
	input()
	k,n,m=takeivr()
	arr1=takeiar()
	arr2=takeiar()
	first=second=0
	ans=[]
	while first<n and second<m:
		# print(first,second)
		if arr1[first]<arr2[second]:
			
			ans.append(arr1[first])
			first+=1
		else:
			
			ans.append(arr2[second])
			second+=1

	for i in range(first,n):
		ans.append(arr1[i])
	for i in range(second,m):
		ans.append(arr2[i])

	for i in range(n+m):
		if ans[i]!=0:

			if k<ans[i]:
				print(-1)
				return 
		else:
			k+=1

	print(*ans)
	return  




	




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