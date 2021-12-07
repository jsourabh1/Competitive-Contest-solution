class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        
        odd=even=0
        
        for i in range(len(position)):
            
            if position[i]%2==0:
                even+=1
                
            else:
                odd+=1
                
        return min(even,odd)


# intuition :- we have to place all the piles in the even position and 
# and all odd piles on the odd position so that this arrangement can be made
              # odd_piles(1) even_piles(0) so it will be the minimum cost


         