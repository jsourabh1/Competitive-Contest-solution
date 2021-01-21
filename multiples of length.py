def solve(arr):
    n=len(arr)
    if len(arr)==1:
        print("1 1")
        print("0")
        print("1 1")
        print("0")
        print("1 1")
        print(-arr[0])


    else:
        print("1 1")
        print(-arr[0])
        arr[0]=0
        print("2 "+str(n))
        for i in range(1,n):
            val=(arr[i]%n)*(n-1)
            print(val,end=" ")
            arr[i]+=val
        print()
        print("1 "+str(n))
        for i in range(n):
            print(int(-arr[i]),end=" ")






n=int(input())
arr=list(map(int,input().split()))
solve(arr)

