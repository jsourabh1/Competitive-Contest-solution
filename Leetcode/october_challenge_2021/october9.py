from collections import defaultdict
class TrieNode():
    
    def __init__(self):
        
        self.children=defaultdict(TrieNode)
        self.isword=False

class solve:
    
    def __init__(self):
        
        self.root=TrieNode()
        
        
    def insert(self,word):
        node=self.root
        
        for w in word:
            node=node.children[w]
        node.isword=True
        
        
def rec(board,node,temp,row,col,string):
    
    if node.isword:
        # print(string)
        temp.append(string)
        node.isword=False
       
    if row<0 or row>=len(board) or col<0 or col>=len(board[0]):
        return
    t=board[row][col]
    node=node.children.get(t)
    
    if not node:
        return 
    board[row][col]="~"
    rec(board,node,temp,row+1,col,string+t)
    rec(board,node,temp,row-1,col,string+t)
    rec(board,node,temp,row,col+1,string+t)
    rec(board,node,temp,row,col-1,string+t)
    board[row][col]=t
    return
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        trie=solve()
        ans=[]
        node=trie.root
        for w in words:
            trie.insert(w)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                rec(board,node,ans,i,j,"")
        return ans
                
                
    
        