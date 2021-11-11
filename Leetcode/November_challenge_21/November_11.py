class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        inital=0
        
        count=0
        for i in nums:
            count+=i
            
            if count<1:
                
                inital+=abs(count)+1
                count=1
                
        return inital if inital!=0 else 1
        
        
        