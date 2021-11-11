def countNodes(root):
    if root is None:
        return 0
    return (1+ countNodes(root.left) + countNodes(root.right))
 
# This function checks if binary tree is complete or not
def isComplete(root, index, number_nodes):
     
    # An empty is complete
    if root is None:
        return True
     
    # If index assigned to current nodes is more than
    # number of nodes in tree, then tree is not complete
    if index >= number_nodes :
        return False
     
    # Recur for left and right subtress
    return (isComplete(root.left , 2*index+1 , number_nodes)
        and isComplete(root.right, 2*index+2, number_nodes)
          )

class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        #Code Here
        
        nodes=countNodes(root)
        
        def helper(root):
        
            if not root:
                return True
                
            if root.left and root.right and root.left.data>=root.data and root.right.data>=root.data:
                return False
                
            elif root.left and root.left.data>=root.data:
                return False
                
            elif root.right and root.right.data>=root.data:
                return False
                
            return helper(root.left) and helper(root.right)
            
            
        
        if isComplete(root,0,nodes):
            
            return helper(root)
        else:
            return False
        