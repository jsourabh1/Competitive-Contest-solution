#User function Template for python3

#Back-end complete function Template for Python 3

from collections import defaultdict

class Solution:
    def RulingPair(self, arr, n): 
    	# Your code goes here
    	
    	dict_1=defaultdict(list)
    	
    	for i in arr:
    	    
    	    temp=0
    	    j=i
    	    while j:
    	        temp+=j%10
    	        j//=10
    	        
    	    dict_1[temp].append(i)
    	    
    	    
    	ans=0
    	 
    	for i in dict_1.keys():
    	     
    	     if len(dict_1[i])>=2:
    	         dict_1[i].sort(reverse=True)
    	         ans=max(ans,dict_1[i][0]+dict_1[i][1])
	         
    	         
    	return ans if ans!=0 else -1
    	    
    	    