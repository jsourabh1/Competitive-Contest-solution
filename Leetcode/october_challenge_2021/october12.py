# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low=0
        
        high=n
        
        while low<high:
            
            mid=(low+high)//2
            
            temp=guess(mid)
            
            if temp==0:
                return mid
            if temp==-1:
                high=mid-1
            else:
                low=mid+1
                
        if guess(low)==0:
            return low
        