#User function Template for python3
class Solution:
	def maxSubstring(self, S):
		# code here
		
		ans=-1
		count0=count1=0
		left=right=0
		while right<len(s):
		    if S[right]=="1":
		        count1+=1
		    else:
		        count0+=1
		    while count0<=count1 and left<right:
		        
		        if S[left]=="1":
		            count1-=1
		        else:
		            count0-=1
		        left+=1
		        
		    ans=max(count0-count1,ans)
		    right+=1
		    
		return ans 