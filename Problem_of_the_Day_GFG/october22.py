#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
from collections import defaultdict

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        # code here
        
        res=[]
        
        
        dict_1=defaultdict(dict)
        
        
        def recursion(root,row,col,dict_1):
            
            
            if not root:
                return 
            if  row not in dict_1[col]:
                dict_1[col][row]=[]
          
            
            dict_1[col][row].append(root.data)
            
            recursion(root.left,row+1,col-1,dict_1)
            recursion(root.right,row+1,col+1,dict_1)
            
            
        recursion(root,0,0,dict_1)
        # print(dict_1)
        for i in sorted(dict_1.keys()):
            res.append(dict_1[i][sorted(dict_1[i].keys())[0]][0])
                    
          
                   
                   
        return res
            