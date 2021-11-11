#Your task is to complete this Function \

class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        
       
        m=len(A)
        n=len(B)
        
        if (m+n)!=len(C):
            return False
        dp=[[False]*(n+1) for i in range(m+1)]
        
        for i in range(m+1):
            
            for j in range(n+1):
                
                if i==0 and j==0:
                    dp[i][j]=True
                    
                elif i==0:
                    if B[j-1]==C[j-1]:
                        dp[i][j]=dp[i][j-1]
                
                elif j==0:
                     
                    if A[i-1]==C[i-1]:
                         
                        dp[i][j]=dp[i-1][j]
                elif A[i-1]==B[j-1]==C[i+j-1]:
                    
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                    
                elif A[i-1]==C[i+j-1]:
                    dp[i][j]=dp[i-1][j]
                    
                elif B[j-1]==C[i+j-1]:
                    dp[i][j]=dp[i][j-1]
                    
        return dp[m][n]
                    
                         
                    
        
            