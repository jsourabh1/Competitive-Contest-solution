# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        count=0
        
        stack=[(root,False)]
        
        while stack:
            
            
            current,is_left=stack.pop()
            
            if not current:
                continue
                
            if not current.left and not current.right:
                
                if is_left:
                    count+=current.val
                    
                    
            else:
                stack.append([current.left,True])
                stack.append([current.right,False])
                
        return count
        