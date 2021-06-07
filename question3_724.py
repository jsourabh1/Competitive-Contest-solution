'''
The tycoon of a winery empire in Mondstadt, unmatched in every possible way. A thinker in the Knights of Favonius with an exotic appearance.

This time, the brothers are dealing with a strange piece of wood marked with their names. This plank of wood can be represented as a string of n characters. Each character is either a 'D' or a 'K'. You want to make some number of cuts (possibly 0) on this string, partitioning it into several contiguous pieces, each with length at least 1. Both brothers act with dignity, so they want to split the wood as evenly as possible. They want to know the maximum number of pieces you can split the wood into such that the ratios of the number of occurrences of 'D' to the number of occurrences of 'K' in each chunk are the same.

Kaeya, the curious thinker, is interested in the solution for multiple scenarios. He wants to know the answer for every prefix of the given string. Help him to solve this problem!

For a string we define a ratio as a:b where 'D' appears in it a times, and 'K' appears b times. Note that a or b can equal 0, but not both. Ratios a:b and c:d are considered equal if and only if a⋅d=b⋅c.

For example, for the string 'DDD' the ratio will be 3:0, for 'DKD' — 2:1, for 'DKK' — 1:2, and for 'KKKKDD' — 2:4. Note that the ratios of the latter two strings are equal to each other, but they are not equal to the ratios of the first two strings.

'''

# DaRk DeveLopeR
import sys

# taking input as string
input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda: list(map(int, sys.stdin.readline().rstrip("\r\n").split()))
mod = 10 ** 9 + 7;
Mod = 998244353;
INF = float('inf')
# ______________________________________________________________________________________________________
from math import *
from bisect import *
from heapq import *
from collections import defaultdict as dd
from collections import OrderedDict as odi
from collections import Counter as cc
from collections import deque
from itertools import groupby

sys.setrecursionlimit(20 * 20 * 20 * 20 + 10)  # this is must for dfs

#question link:- https://codeforces.com/contest/1536/problem/C


def solve():
    n = takein()

    string =takesr()
    dict_1=dd(lambda:0)

    d=k=0
    for i in string:

        if i=="D":
            d+=1
        else:
            k+=1
        x,y=d,k
        g=gcd(x,y)
        x//=g
        y//=g
        string=str(x)+":"+str(y)
       
        dict_1[string]+=1

        print(dict_1[string],end=" ")
    print()


def main():
    global tt

    t = 1
    t = takein()
    # t = 1
    for tt in range(1, t + 1):
        solve()


# ---------------------- USER DEFINED INPUT FUNCTIONS ----------------------#
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


# ------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#


def ispalindrome(s):
    return s == s[::-1]


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
    rslt = bin(inverse_s)[3:]

    return str(rslt)


def counter(a):
    q = [0] * max(a)
    for i in range(len(a)):
        q[a[i] - 1] = q[a[i] - 1] + 1
    return (q)


def counter_elements(a):
    q = dict()
    for i in range(len(a)):
        if a[i] not in q:
            q[a[i]] = 0
        q[a[i]] = q[a[i]] + 1
    return (q)


def string_counter(a):
    q = [0] * 26
    for i in range(len(a)):
        q[ord(a[i]) - 97] = q[ord(a[i]) - 97] + 1
    return (q)


def factorial(n, m=1000000007):
    q = 1
    for i in range(n):
        q = (q * (i + 1)) % m
    return (q)


def factors(n):
    q = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0: q.append(i); q.append(n // i)
    return (list(sorted(list(set(q)))))


def prime_factors(n):
    q = []
    while n % 2 == 0: q.append(2); n = n // 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0: q.append(i); n = n // i
    if n > 2: q.append(n)
    return (list(sorted(q)))


def transpose(a):
    n, m = len(a), len(a[0])
    b = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][i]
    return (b)


def power_two(x):
    return (x and (not (x & (x - 1))))


def ceil(a, b):
    return -(-a // b)


def seive(n):
    a = [1]
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p = p + 1
    for p in range(2, n + 1):
        if prime[p]:
            a.append(p)
    return (a)


# -----------------------------------------------------------------------#
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    input = sys.stdin.readline

main()
