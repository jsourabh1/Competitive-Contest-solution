#User function Template for python3



'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to count number of subtrees having sum equal to given sum.
def countSubtreesWithSumX(root, X):
    
    ans=0
    def helper(root,X):
        nonlocal ans
        
        if not root:
            return 0,True
            
        left,flag=helper(root.left,X)
        if left==X and not flag:
            ans+=1
        right,flag=helper(root.right,X)
        
        if right==X and not flag:
            ans+=1
        summ=root.data+left+right 
        ok=False
        if summ==X:
            ans+=1
            ok=True
            
        return summ,ok
            
        
        
    helper(root,X)
    return ans