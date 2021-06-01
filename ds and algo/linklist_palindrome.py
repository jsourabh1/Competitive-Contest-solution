import sys

# taking input as string
# input = lambda: sys.stdin.readline().rstrip("\r\n")
# inp = lambda: list(map(int,sys.stdin.readline().rstrip("\r\n").split()))
import time

mod = 10 ** 9 + 7;
Mod = 998244353;
INF = float('inf')


# ______________________________________________________________________________________________________
# from math import *
# from bisect import *
# from heapq import *
# from collections import defaultdict as dd
# from collections import OrderedDict as odict
# from collections import Counter as cc
# from collections import deque
# from itertools import groupby
# sys.setrecursionlimit(20*20*20*20+10) #this is must for dfs


def isPalindrome(head) -> bool:
    stack = []

    slow = head

    while slow != None:
        stack.append(slow.val)

        slow = slow.next
    p = True
    start = head
    while len(stack) > 0:
        l = stack.pop()

        if start.val != l:
            p = False
            break
        print(l, start.val)
        print(stack)

    return p


def solve():
    n, k = 6,10
    #n, k = takeivr()
    #arr = takeiar()
    arr = [2,8,8 ,2 ,2,8]

    arr.sort(reverse=True)
    #print(arr)


    count = 0
   

    while len(arr) > 0:

        height = k
        i = 0
        while height > 0 and len(arr) > 0 and i<len(arr):
            if arr[i] <= height:
                height -= arr[i]
                arr.remove(arr[i])
            i+=1

        #print(arr)
        count += 1
    


    print(count)


def main():
    global tt
    if not ONLINE_JUDGE:
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    t = 1
    #t = takein()
    #t = 1
    for tt in range(1, t + 1):
        solve()
    if not ONLINE_JUDGE:
        # print("Time Elapsed :",time.time() - start_time,"seconds")
        sys.stdout.close()


# ---------------------- USER DEFINED INPUT FUNCTIONS ----------------------#
# for the itnteger input
def takein():
    return (int(sys.stdin.readline().rstrip("\r\n")))


# input the string

def takesr():
    return (sys.stdin.readline().rstrip("\r\n"))


# input int array
def takeiar():
    return (list(map(int, sys.stdin.readline().rstrip("\r\n").split())))


# input sttring array
def takesar():
    return (list(map(str, sys.stdin.readline().rstrip("\r\n").split())))


# innut values for the diffrent variables
def takeivr():
    return (map(int, sys.stdin.readline().rstrip("\r\n").split()))


def inpsvr():
    return (map(str, sys.stdin.readline().rstrip("\r\n").split()))


# ------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#
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
