# Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

# Input: nums = ["777","7","77","77"], target = "7777"
# Output: 4
# Explanation: Valid pairs are:
# - (0, 1): "777" + "7"
# - (1, 0): "7" + "777"
# - (2, 3): "77" + "77"
# - (3, 2): "77" + "77"
# Example 2:


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        count=0
        
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                
                if i!=j and nums[i]+nums[j]==target:
                    count+=1
                    
        return count
                    