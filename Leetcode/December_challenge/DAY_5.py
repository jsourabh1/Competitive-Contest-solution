# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#getting wrong ans on this approach but still working on 

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:
            return 
        
        queue=[]
        
        queue.append(root)
        
        even=odd=0
        count=0
        while queue:
            
        
            count1=len(queue)
            
            
            while count1:
                
                if count%2==0:
                    
                    node=queue.pop(0)
                    
                    even+=node.val
                    
                else:
                    node=queue.pop(0)
                    odd+=node.val
                    
                    
                if node.right:

                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)
                
                count1-=1
            print(even,odd)                
            count+=1
            
        return max(even,odd)
                
                
            
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    
    def __init__(self):
        self.dict_1=defaultdict()
    
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:
            return 0
        
        if root in self.dict_1:
            
            return self.dict_1[root]
        
        
        val=0
        
        if root.left:
            
            val+=self.rob(root.left.left)+self.rob(root.left.right)
            
        if root.right:
            
            val+=self.rob(root.right.left)+self.rob(root.right.right)
            
            
        val=max(val+root.val,self.rob(root.left)+self.rob(root.right))
        
        self.dict_1[root]=val
        
        return val
        
        

