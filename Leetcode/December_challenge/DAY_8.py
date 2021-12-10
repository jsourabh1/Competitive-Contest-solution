# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        
        def helper(root,sum2):
            
            if not root:
                return 0
            temp=0
            left=helper(root.left,sum2)
            right=helper(root.right,sum2)
            temp=root.val+left+right
            root.val=abs(left-right)
            sum2[0]+=root.val
            
            
            
            return temp
        
        sum2=[0]
        helper(root,sum2)
        # print(summ,sum2)
        return sum2[0]
        