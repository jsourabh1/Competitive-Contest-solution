class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        left,right=0,n
        
        while left<=right:
            
            mid=(left+right)//2
            
            temp=mid*(mid+1)//2
            print(temp,mid,left,right)
            if temp==n:
                print(temp,mid,left,right)
                return mid
            if n<temp:
                right=mid-1
                
            else:
                left=mid+1
                
        return right
                
        