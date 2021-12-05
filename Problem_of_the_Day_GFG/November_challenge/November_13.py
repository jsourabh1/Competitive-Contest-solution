
#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        
        stack=[]
        temp=["[","{","("]
        
        for i in x:
            if i in temp:
                stack.append(i)
            else:
                
                if not stack or(  i==")" and stack[-1]!="("):
                    return False
                elif not stack or (i=="}" and stack[-1]!="{"):
                    return False
                elif not stack or  (i=="]" and stack[-1]!="["):
                    return False
                else:
                    stack.pop() 
                    
        if not stack:
            return True
        return False        
                    