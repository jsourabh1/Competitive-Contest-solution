
                #question for practisehttps://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/        
def ispalin(string):
    first=0
    second=len(string)-1
    
    while first<second:
        
        if string[first]!=string[second]:
            return False
        first+=1
        second-=1
    return True
        

class Solution:

    
    def maxProduct(self, s: str) -> int:
        self.ans=0
        
        def backtrack(string,string1,string2,index):
            
            if index>=len(string):
                
                if ispalin(string1) and ispalin(string2):
                    self.ans=max(self.ans,len(string1)*len(string2))
                return 
            
            
            backtrack(string,string1+string[index],string2,index+1)
            backtrack(string,string1,string2+string[index],index+1)
            backtrack(string,string1,string2,index+1)
        backtrack(s,"","",0)
        return self.ans
        
        