class Solution:
    def fib(self, n: int) -> int:
        # first approach: simple recursion:
        '''
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
        '''
        
        # first approach is bad because it is taking O(2^n) time
        # we can save this space and time by identifying sub problems that are being solved repeatedly and storing them
        # this will require a memoisation approach, with three steps with an inner helper function to keep a single dp array : declare dp array, check if subproblem stored, if not store and return it
        
        '''
        dp = [None] * (n + 1)
        def helper(n):
            if dp[n]:
                return dp[n]
            if n <= 1:
                return n
            result = helper(n - 1) + helper(n - 2)
            dp[n] = result
            return result
        return helper(n)
        '''
        # Recursion with memoisation brings the complexity down to O(n) space but the stack call space is still O(n) we can further optimise the recursion into a dp approach
        # init the same dp array as the memoisation, start from the basecase and then go up to the desired solution by converting the recursive relation into an expression
        if n <= 1:
            return n
        dp = [None] * (n + 1)
        # now we can insert the basecases here
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] # changing the recursive relation into an expression
        return dp[n]