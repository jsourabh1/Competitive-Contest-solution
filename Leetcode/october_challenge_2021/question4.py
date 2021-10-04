#short solution:- 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        if M==N==1:
            return 4
        count=0
        for i in range(M):
            
            for j in range(N):
                
                if grid[i][j]==1:
                
                    
                    if j==N-1 or  grid[i][j+1]==0:
                        count+=1

                    if j==0 or grid[i][j-1]==0:
                        count+=1

                    if i==M-1 or  grid[i+1][j]==0:
                        count+=1
                    if i==0 or grid[i-1][j]==0:
                        count+=1
        return count

# understanding solution 

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        if M==N==1:
            return 4
        count=0
        for i in range(M):
            
            for j in range(N):
                
                if grid[i][j]==1:
                
                    if i==0:
                        count+=1
                    if j==0:
                        count+=1
                    if i==M-1:
                        count+=1
                    if j==N-1:
                        count+=1
                    if j<N-1 and grid[i][j+1]==0:
                        count+=1

                    if j>0 and grid[i][j-1]==0:
                        count+=1

                    if i<M-1 and grid[i+1][j]==0:
                        count+=1
                    if i>0 and grid[i-1][j]==0:
                        count+=1
        return count