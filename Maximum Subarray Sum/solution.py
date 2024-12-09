class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        this is a simple dynamic programming problem that can be solved using the kadanes algorithm with dynamic programming
        '''
        local_maxima = nums[0]
        global_maxima = nums[0]
        for num in nums[1:]:
            local_maxima = max(num, num + local_maxima)
            global_maxima = max(local_maxima, global_maxima)
        return global_maxima
        
        