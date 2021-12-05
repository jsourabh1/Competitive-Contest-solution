def solve(nums,index,dp):
    
    if index>=len(nums):
        return 0
    
    if dp[index]!=-1:
        return dp[index]
    
    dp[index]=nums[index]+max(solve(nums,index+2,dp),solve(nums,index+3,dp))
    
    return dp[index]




class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp=[-1]*len(nums)
        
        return max(solve(nums,0,dp),solve(nums,1,dp))