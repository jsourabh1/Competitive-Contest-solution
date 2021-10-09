#User function Template for python3
class Solution:
	def minPoints(self, points, M, N):
		# code here
		
		dp=[[0]*N for i in range(M)]
		
		dp[-1][-1]=max(1,1-points[-1][-1])
		
		for i in range(M-2,-1,-1):
		    
		    dp[i][N-1]=max(1,dp[i+1][N-1]-points[i][N-1])
		    
		for i in range(N-2,-1,-1):
		    
		    dp[M-1][i]=max(1,dp[M-1][i+1]-points[M-1][i])
	    
	    for i in range(M-2,-1,-1):
	        
	        for j in range(N-2,-1,-1):
	            
	            minn=min(dp[i+1][j],dp[i][j+1])
	            
	            dp[i][j]=max(1,minn-points[i][j])
	            
	    return dp[0][0]