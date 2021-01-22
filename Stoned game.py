def solve():
    return


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    maxx=max(arr)
    suum=sum(arr)
    if suum%2!=0 or (maxx>(suum-maxx)):
        print("T")
    else:
        print("HL")



