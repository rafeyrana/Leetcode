class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        this is a classic dp problem, we will go in reverse to try and solve this in the dp array we store the number of jumps needed to get to the goal for each index we check if the goal is in the range of the i + nums[i] we change the dp of that to 1 if that is not the case then we go through the range i + 1 - i + nums[i] which are all the indices we can possibly jump to from that and choose the minimum value for the jump and add 1 to it fro jumping to it  and assign it to the dp array so we know that we have to jump to that one this will be done in a reverse loop
        ''' 
        if len(nums) == 1:
            return 0
        dp = [102 for _ in nums] # 102 is because the range of i is less than 101
        for i in range(len(nums)- 1, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                dp[i] = 1
                continue
            for k in range(i + 1, i + nums[i] + 1):
                dp[i] = 1 + min(dp[k], dp[i] - 1)
        return dp[0]
        