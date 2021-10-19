# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        
        def helper(root,parent,depth,value):
            if root:
                
                if root.val==value:
                    return parent,depth
                
                return helper(root.left,root,depth+1,value) or helper(root.right,root,depth+1,value)
            
        first,second,third,fourth=helper(root,None,0,x) +helper(root,None,0,y)
        
        return first!=third and second==fourth
        