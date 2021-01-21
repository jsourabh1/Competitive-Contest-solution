from collections import defaultdict
def solve():
    return


for _ in range(int(input())):
    n=int(input())
    dic=defaultdict()
    for i in range(n):
        arr=list(map(str,input().strip()))
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
    flag=1
    for i in dic.values():
        if i%n!=0:
            flag=0
            print("NO")
            break

    if flag==1:
        print("YES")


