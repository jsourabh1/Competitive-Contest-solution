# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, arr: List[int]) -> TreeNode:
        
        def construct(root,key):
            
            if not root:
                return TreeNode(key)
            
            
            if root.val>key:
            
                root.left=construct(root.left,key)
            else:
                root.right=construct(root.right,key)
            
            return root
        
        root=None
        for i in arr:
            root=construct(root,i)
            
        return root
        