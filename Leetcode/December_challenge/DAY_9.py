#brute form doone from dfs and recursion 



class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        
        
        def helper(arr,index):
            
            if 0<=index<len(arr) and arr[index]>=0:
                
                arr[index]=-arr[index]
                return arr[index]==0 or helper(arr,index+arr[index]) or helper(arr,index-arr[index])
            return False
        
        return helper(arr,start)
        
        
        