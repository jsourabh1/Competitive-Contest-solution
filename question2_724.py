'''
I, Fischl, Prinzessin der Verurteilung, descend upon this land by the call of fate an — Oh, you are also a traveler from another world? Very well, I grant you permission to travel with me.

It is no surprise Fischl speaks with a strange choice of words. However, this time, not even Oz, her raven friend, can interpret her expressions! Maybe you can help us understand what this young princess is saying?

You are given a string of n lowercase Latin letters, the word that Fischl just spoke. You think that the MEX of this string may help you find the meaning behind this message. The MEX of the string is defined as the shortest string that doesn't appear as a contiguous substring in the input. If multiple strings exist, the lexicographically smallest one is considered the MEX. Note that the empty substring does NOT count as a valid MEX.

A string a is lexicographically smaller than a string b if and only if one of the following holds:

a is a prefix of b, but a≠b;
in the first position where a and b differ, the string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
A string a is a substring of a string b if a can be obtained from b by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

Find out what the MEX of the string is!




'''


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

#question link:-https://codeforces.com/contest/1536/problem/B

def helper():

	one=[0]*27
	two=[0]*(27*27)
	three=[0]*(27*27*27)

	for i in range(26):
		one[i]=chr(ord('a')+i)

		for j in range(0,26):
			two[26*i+j]=one[i]+chr(ord('a')+j)

			for k in range(26):
				three[26*26*i+26*j+k]=two[j]+chr(ord('a')+k)

	return one,two,three
def solve(one,two,three):

	n=takein()

	string=takesr()

	dict_1=dd(lambda:0)

	for i in string:

		dict_1[i]=1

	prev=0
	for i in range(2,n+1):

		dict_1[string[prev:i]]=1
		prev+=1

	prev=0
	

	for i in range(3,n+1):

		dict_1[string[prev:i]]=1
		prev+=1

	
	ans=None

	for i in range(26):

	 	if dict_1[one[i]]==0:
	 		ans=one[i]
	 		break

	if ans is None:

	 	for i in range(26*26):
	 		

	 		if dict_1[two[i]]==0:
	 			ans=two[i]
	 			break

	if ans is None:

	 	for i in range(26*26*26):

	 		if dict_1[three[i]]==0:
	 			ans=three[i]
	 			break

	if ans is None:

	 	print("No")
	else:
	 	print(ans)






	




def main():
 global tt
 if not ONLINE_JUDGE:
     sys.stdin = open("input.txt","r")
     sys.stdout = open("output.txt","w")
 t = 1
 one,two,three=helper()
 t = takein()
 #t = 1
 for tt in range(1,t + 1):
     solve(one,two,three)
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
#-----------------------------------------------------------------------#
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
 input = sys.stdin.readline
 
main()