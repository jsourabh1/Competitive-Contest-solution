class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        
        
        if not root:
            return None
            
        if root.data==n1 or root.data==n2:
            return root
            
        left=self.lca(root.left,n1,n2)
        right=self.lca(root.right,n1,n2)
        
        if left and right:
            return root
            
        return left if left is not None else right
