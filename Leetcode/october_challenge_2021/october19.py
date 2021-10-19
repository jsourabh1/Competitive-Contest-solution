class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        stack=[]
        next_greater={}
        for i in nums2[::-1]:
            
            
            while stack and stack[-1]<i:
                
                stack.pop()
                
            if not stack:
                next_greater[i]=-1
            else:
                next_greater[i]=stack[-1]
                
            stack.append(i)
        
        ans=[]
        
        for i in nums1:
            
            ans.append(next_greater[i])
            
        return ans
        
        
                
        