from bisect import bisect
class Solution:
    def ValidPair(self, arr, n): 
    	# Your code goes here
    # 	count=0
    # 	for i in range(n):
    	    
    # 	    for j in range(i+1,n):
    	        
    # 	        if arr[i]+arr[j]>0:
    # 	            count+=1
    # 	return count
    
        arr.sort()
        count=0
        for i in range(n):
            
            if arr[i]<0:
                
                index=bisect(arr,-arr[i])
                # print(index)
                count+=n-index 
            else:
                break
        # print(i)
        temp=n-i
        count+=(temp*(temp-1))//2
        return count