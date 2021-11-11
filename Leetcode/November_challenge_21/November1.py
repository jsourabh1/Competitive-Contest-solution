class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row=len(board)
        
        if not row:
            return 
        
        col=len(board[0])
        
        
        for i in range(row):
            
            check(board,i,0,row,col)
            
            if col>1:
                
                check(board,i,col-1,row,col)
                
        for j in range(col):
            
            check(board,0,j,row,col)
            if row>1:
                
                check(board,row-1,j,row,col)
                
                
                
                
        for i in range(row):
            
            for j in range(col):
                
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="1":
                    
                    board[i][j]="O"
                    
                    
def check(board,i,j,row,col):
    
    if board[i][j]=="O":
        
        board[i][j]="1"
        
        if i>1:
            
            check(board,i-1,j,row,col)
            
        if j>1:
            
            check(board,i,j-1,row,col)
            
        if j<col-1:
            check(board,i,j+1,row,col)
            
        if i<row-1:
            
            check(board,i+1,j,row,col)
            
            
                    
            
        