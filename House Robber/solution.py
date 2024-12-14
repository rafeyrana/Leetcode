class Solution:
    def rob(self, nums: List[int]) -> int:
        # okay so in this case we have two options for our dp array, either we rob this current house and the house 2 is back or not this house and just rob the house at i - 1
        dp = [0] * len(nums)
        dp[0] = nums[0] # either this can be robbed
        if len(nums) == 1:
            return dp[-1]
        dp[1] = max(nums[0], nums[1]) # or this can be robbed, both cannot be robbed at the same time
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
        