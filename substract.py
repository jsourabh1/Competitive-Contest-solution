import math


def prime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True


    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = i5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

for _ in range(int(input())):

    n=int(input())
    count=0
    while n!=1:

        if n%2!=0:
            n-=1
            count+=1
        else:
            n=2
            count+=1

    print(count)
