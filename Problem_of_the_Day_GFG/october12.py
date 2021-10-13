from collections import defaultdict
class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here
        
        arr.sort()
        
        count=0
        
        for i in range(0,n-2):
            
            j=i+1
            k=n-1
            
            while j<k:
                
                if arr[i]+arr[j]+arr[k]>=sumo:
                    k-=1
                else:
                    count+=(k-j)
                    j+=1
        return count