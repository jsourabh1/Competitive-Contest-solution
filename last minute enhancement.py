
for _ in range(int(input())):
    
    n=int(input())
    arr=list(map(int,input().split()))
    s=set()
    
    for i in arr:
        if i not in s:
            s.add(i)
        elif (i+1) not in s:
            s.add(i+1)
            
    print(len(s))