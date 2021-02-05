#wihtour dp only the recursion 

'''
def rec(arr,n,sum):

    if sum==0:
        return True
    if n==0:
        return False
    
    if arr[n]>sum:

        return rec(arr,n-1,sum)
    return rec(arr,n-1,sum-arr[n]) or rec(arr,n-1,sum)





# with dp (memoziaton)
def rec(arr,n,sum,t):

    if sum==0:
        return True
    if n==0:
        return False
   

    if t[n][sum]!=-1:
        return t[n][sum]
    
    if arr[n-1]>sum:

        return rec(arr,n-1,sum,t)
    return rec(arr,n-1,sum-arr[n-1],t) or rec(arr,n-1,sum,t)

'''
#dp with topdown apprach


def rec(arr,n,sum):
    t=[[-1 for i in range(sum+1)] for j in range(n+1)]
        

    for i in range(n+1):
        for j in range(sum+1):
            #print(t[i][j])

            if i==0 and j==0:

                t[i][j]=True
            elif j==0:

                t[i][0]=True

            elif i==0:


                t[0][j]=False
            
    for i in range(1,n+1):
        for j in range(1,sum+1):

            if arr[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]

   

    print(t[n][sum])
    



for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    
    if sum(arr)%2!=0:
        print(False)
    
    else:
      
        rec(arr,n,sum(arr)//2)