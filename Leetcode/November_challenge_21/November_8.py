class Solution:
    def numTrees(self, n: int) -> int:
        
        if n==1 or n==0:
            return 1
        
        catlan=[0]*(n+1)
        
        catlan[0]=1
        catlan[1]=1
        
        for i in range(2,n+1):
            
            for j in range(i):
                
                catlan[i]+=catlan[j]*catlan[i-j-1]
                
        return catlan[n]