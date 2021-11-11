class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        visit=set()
        start=()
        end=()
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j]==0:
                    visit.add((i,j))
                if grid[i][j]==1:
                    start=(i,j)
                    
                if grid[i][j]==2:
                    end=(i,j)
                    visit.add((i,j))

                    

         

        def solve(i,j,visit):
            
    
            print(path)
            if (i,j)==end: 
                return len(visit)==0
                
            ans=0
            if (i+1,j) in visit:

                
                visit.remove((i+1,j))
                ans+=solve(i+1,j,visit)
                visit.add((i+1,j))
                
            if (i-1,j) in visit:

                
                visit.remove((i-1,j))
                ans+=solve(i-1,j,visit)
                visit.add((i-1,j))
                
                
            if (i,j+1) in visit:

                
                visit.remove((i,j+1))
                ans+=solve(i,j+1,visit)
                visit.add((i,j+1))
                
                
            if (i,j-1) in visit:

                
                visit.remove((i,j-1))
                ans+=solve(i,j-1,visit)
                visit.add((i,j-1))
                
                
            return ans
                
           

        
        return solve(start[0],start[1],visit)
        
       
                    

                    


from collections import defaultdict
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        count=0
        
        for i in range(len(word)):
            
            if word[i] not in ["a","e","i","o","u"]:
                continue
            s=set()
            
            s.add(word[i])
            
            for j in range(i+1,len(word)):
                s.add(word[j])
                
                if len(s)==5:count=+=1
                    
                    
        return count
                
            
obj=Solution()
obj.countVowelSubstrings("aeiouu")
        
        
        
        