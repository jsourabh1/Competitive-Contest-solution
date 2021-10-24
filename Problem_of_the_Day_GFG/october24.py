#User function Template for python3
from heapq import *
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, vertex,graf):
        #code here
        
        key=[float("inf")]*vertex
       
        parent=[0]*vertex
        mset=[False]*vertex
        
        key[0]=0
        
        
        parent[0]=-1
        
       
        heap=[]
        heap.append([0,0])
        heapify(heap)
        while heap:
            
            cost,node=heappop(heap)
            
            if mset[node]:
                continue
            
            mset[node]=True
            
            for j,cost1 in graf[node]:
                
                if key[j]>cost1 and mset[j]==False:
                    key[j]=cost1
                    parent[j]=node
                    heappush(heap,[cost1,j])
        # print(key)
        return sum(key)
        