#DaRk DeveLopeR


'''



C. Pursuit
time limit per test2 seconds
memory limit per test512 megabytes
inputstandard input
outputstandard output
You and your friend Ilya are participating in an individual programming contest consisting of multiple stages. A contestant can get between 0 and 100 points, inclusive, for each stage, independently of other contestants.

Points received by contestants in different stages are used for forming overall contest results. Suppose that k stages of the contest are completed. For each contestant, k−⌊k4⌋ stages with the highest scores are selected, and these scores are added up. This sum is the overall result of the contestant. (Here ⌊t⌋ denotes rounding t down.)

For example, suppose 9 stages are completed, and your scores are 50,30,50,50,100,10,30,100,50. First, 7 stages with the highest scores are chosen — for example, all stages except for the 2-nd and the 6-th can be chosen. Then your overall result is equal to 50+50+50+100+30+100+50=430.

As of now, n stages are completed, and you know the points you and Ilya got for these stages. However, it is unknown how many more stages will be held. You wonder what the smallest number of additional stages is, after which your result might become greater than or equal to Ilya's result, at least in theory. Find this number!

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤1000). Description of the test cases follows.

The first line of each test case contains a single integer n (1≤n≤105) — the number of completed stages.

The second line contains n integers a1,a2,…,an (0≤ai≤100) — your points for the completed stages.

The third line contains n integers b1,b2,…,bn (0≤bi≤100) — Ilya's points for the completed stages.

It is guaranteed that the sum of n over all test cases does not exceed 105.

Output
For each test case print a single integer — the smallest number of additional stages required for your result to be able to become greater than or equal to Ilya's result.

If your result is already not less than Ilya's result, print 0.

Example
inputCopy
5
1
100
0
1
0
100
4
20 30 40 50
100 100 100 100
4
10 20 30 40
100 100 100 100
7
7 59 62 52 27 31 55
33 35 50 98 83 80 64
outputCopy
0
1
3
4
2
Note
In the first test case, you have scored 100 points for the first stage, while Ilya has scored 0. Thus, your overall result (100) is already not less than Ilya's result (0).

In the second test case, you have scored 0 points for the first stage, while Ilya has scored 100. A single stage with an opposite result is enough for both your and Ilya's overall scores to become equal to 100.

In the third test case, your overall result is 30+40+50=120, while Ilya's result is 100+100+100=300. After three additional stages your result might become equal to 420, while Ilya's result might become equal to 400.

In the fourth test case, your overall result after four additional stages might become equal to 470, while Ilya's result might become equal to 400. Three stages are not enough.

question link:- https://codeforces.com/contest/1530/problem/C

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

	n=takein()
	a=takeiar()
	b=takeiar()
	heapify(a)
	heapify(b)
	sum_a=sum(a)
	sum_b=sum(b)
	rem=math.ceil(n//4)
	extra=[]
	# print(a,b)
	# print(rem)
	while rem>0:
		first=heappop(a)
		second=heappop(b)
		sum_a-=first
		sum_b-=second
		extra.append(second)
		# heappop(a)
		# heappop(b)
		rem-=1
	ans=0
	while sum_a<sum_b:
		ans+=1
		sum_a+=100
		sum_b+=0
		n+=1

		if n%4==0:
			sum_a-=heappop(a)

		else:

			if len(extra)>0:
				sum_b+=extra.pop()
	print(ans)








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