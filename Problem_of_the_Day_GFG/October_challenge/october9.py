#User function Template for python3

# You are required to complete this fucntion
# Function should return an integer
import math
class Solution:
    def findK(self, a, n, m, k):
        # Your code goes here
        

        
        
        rowstart=0
        rowend=len(matrix)-1
        colstart=0
        colend=len(matrix[0])-1
        ans=[]
        while rowstart<=rowend and colstart<=colend:
            
            #traverse right
            
            for i in range(colstart,colend+1):
                ans.append(matrix[rowstart][i])
                
            rowstart+=1
            
            #traverse down
            
                
            for i in range(rowstart,rowend+1):
                
                ans.append(matrix[i][colend])
                
            colend-=1
            
            #traverse left
            if (rowstart <= rowend):
                for i in range(colend,colstart-1,-1):
                    ans.append(matrix[rowend][i])
            rowend-=1
            
            
            #traverse up
            if (colstart <= colend):
                for i in range(rowend,rowstart-1,-1):
                    ans.append(matrix[i][colstart])
                
            colstart+=1
            # print(rowstart,rowend,colstart,colend)
        return ans[k-1]
            