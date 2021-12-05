class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=[]
        temp=temperatures[::-1]
        ans=[]
        for i in range(len(temp)):
            
            while stack and stack[-1][0]<=temp[i]:
                stack.pop()
                
            if not stack:
                ans.append(0)
            else:
                ans.append(i-stack[-1][1])
            stack.append([temp[i],i])
                
        return ans[::-1]
            
        