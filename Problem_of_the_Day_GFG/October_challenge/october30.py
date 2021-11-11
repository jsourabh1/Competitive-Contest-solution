from heapq import *
def kthSmallest(mat, n, k): 
    # Your code goes here
    heap=[]
    heapify(heap)
    n=len(mat)

    for i in range(n):
        heappush(heap,[mat[i][0],i,0])


    count=0
    while heap:
        temp,row,col=heappop(heap)

        if count==k-1:
            return temp

        elif col+1<n:
            heappush(heap,[mat[row][col+1],row,col+1])

        count+=1
            