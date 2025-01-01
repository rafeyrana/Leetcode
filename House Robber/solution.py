class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        since in this problem we have to explore all the possible ways to get the max this will be a recursive problem.

        we will be solving this in all the ways possible to optimise a recursion problem:
        1. simple recursion
        2. recursion + memoisation (top down)
        3. tabulation (bottom up)
        '''

        '''
        simple recursion:
        1. arrange everything in reverse index forms: since we have an array this is already done
        2. perform possible actions: two actions either we rob this house and then call the function on a house like n - 2 OR dont rob this house and call the function on the n - 1 house.
        3. optimise for max: take the max of the pick this or not pick this option and return it
        '''

        '''
        def helper(idx):
            if idx < 0:
                return 0
            if idx == 0:
                return nums[0]
            # step 2: perform possible actions
            pick = nums[idx] + helper(idx - 2)
            not_pick = 0 + helper(idx - 1)
            # step 3: optimise
            return max(pick , not_pick)
        return helper(len(nums) - 1) # top down approach so start from the end

        '''

        '''
        we can identify that this problem has repeated subproblems being solved by looking at the recursion tree. (helper function called on idx - 2 which for the previous call can be idx - 1 and so on showing repetition)
        Memoisation:
        1. declare dp array
        2. insert check for dp at this index
        3. store results for this index in dp array
        '''

        '''
        dp = [None] * len(nums)  # Step 1: Initialize memoization table
        
        def helper(idx):
            # Base cases
            if idx < 0:
                return 0
            if idx == 0:
                return nums[0]
            
            # Step 2: Check memoization
            if dp[idx] is not None:
                return dp[idx]
        
            not_pick = helper(idx - 1)  
            pick = nums[idx] + helper(idx - 2)
            
            # Step 3: Store result in memoization table
            dp[idx] = max(pick, not_pick)
            return dp[idx]
        
        return helper(len(nums) - 1)

        '''

        '''
        now that we have solved this using memoisation we can convert this into a tabulation
        1. init same dp array
        2. start by observing basecases and resolve them: ind = -1 and ind = 0
        3. Setup loop and convert the recursive call expression into dp
        '''
        dp = [None] * (len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            pick = nums[i] + (dp[i - 2] if i - 2 >= 0 else 0) # this is because it can go to -1 in case of i = 1
            not_pick = dp[i - 1]
            dp[i] = max(pick, not_pick)
        return dp[-1]

                