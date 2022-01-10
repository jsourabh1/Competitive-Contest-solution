from math import *
for _ in range(int(input())):

    n,m=map(int,input().split())
    
    if ceil(n/2)<m:
        print(-1)
        continue

    board=[['.']*n for i in range(n)]
    index=0

    for i in range(0,n,2):
        board[i][index]="R"
        m-=1
        if m==0:
            break
        index+=2

    for i in range(n):
        print("".join(board[i]))

    
    
