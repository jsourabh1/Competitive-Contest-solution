class Solution:
	def editDistance(self, s, t):
		# Code here
		
		dp=[[0]*(len(s)+1) for i in range(len(t)+1)]
		
		for i in range(len(t)+1):
		    
		    for j in range(len(s)+1):
		        
		        if i==0 and j==0:
		            dp[i][j]=0
		        elif i==0:
		            dp[i][j]=j
		               
		        elif j==0:
		            dp[i][j]=i
		            
		        elif t[i-1]==s[j-1]:
		            
		            dp[i][j]=dp[i-1][j-1]
		        else:
		            
		            dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
		            
		return dp[-1][-1]