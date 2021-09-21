#DaRk DeveLopeR
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

	a,b,c,m=takeivr()
	if (a + b + c - 3 < m):
		print("NO")
		return
	if (a + b + c - 3 ==  m):
		print("YES")
		return
	else:
		if (c > a + b + m + 1 or  b > a + c + m + 1 or  a > b + c + m + 1):
			print("NO")
		else:
			print("YES")







	




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