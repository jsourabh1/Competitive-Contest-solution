# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        
        
        def helper(root,path):
            
            nonlocal summ
            if not root:
                return 
            path.append(str(root.val))
            # print(path)
            helper(root.left,path)
            
            helper(root.right,path)
            
            if not root.right and not root.left:
                summ+=int("".join(map(str,path)))
            
            path.pop()
            
            
        summ=0
        
        helper(root,[])
        return summ
            
            
        