# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
       
        self.dia=0
        def helper(root):
            if not root:
                return 0
            
            left=helper(root.left)
            right=helper(root.right)
            
            self.dia=max(self.dia,1+left+right)
            return 1+max(left,right)
        helper(root)
        return self.dia-1