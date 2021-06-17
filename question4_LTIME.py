

'''
There are N subatomic particles lined up in a row. There are two types: protons and electrons. Protons have a positive charge and are represented by 1, while electrons have a negative charge and are represented by 0.

Our current understanding of physics gives us a way to predict how the particles will be spaced out, if we know their charges. Two adjacent particles will be separated by 1 unit if they have opposite charges, and 2 units if they have the same charge.

When Chef is not in the kitchen, he is doing physics experiments on subatomic particles. He is testing the hypothesis by having N particles in a row, and he will change the charge of a particle K times. In the i-th update, he will change the charge of the Qi-th particle. After each update, find the distance between the first and last particle.

Note: Each update is persistent for further updates.

'''


qeustion link:-https://www.codechef.com/LTIME96C/problems/CHARGES







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


	n,k=takeivr()

	arr_1=list(map(str,input().strip()))

	arr_2=takeiar()

	ans=0
	for i in range(n-1):

		if arr_1[i]==arr_1[i+1]:
			ans+=2
		else:
			ans+=1
	print(ans,arr_1)

	for i in range(k):

		num=arr_2[i]

		if arr_1[num-1]=='1':

			arr_1[num-1]=='0'

			if (num-2)>=0:

				if arr_1[num-2]=='0':
					ans+=1
				else:
					ans-=1
			print("fist",ans)
			if num<n:

				if arr_1[num]=='0':
					ans+=1
				else:
					ans-=1
			print("first",ans)
		else:

			arr_1[num-1]='1'

			if num-2>=0:

				if arr_1[num-2]=='0':
					ans-=1
				else:
					ans+=1
			print("second",ans)
			if num<n:

				if arr_1[num]=='0':
					ans-=1
				else:
					ans+=1
			print(ans)
		print(ans)

	

	




def main():
    global tt
    
    t = 1
    t = takein()
    #t = 1
    for tt in range(1,t + 1):
        solve()
   

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
#-----------------------------------------------------------------------#
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    input = sys.stdin.readline
    
main()