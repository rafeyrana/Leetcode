class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        this is a simple fibonnaci sequence modelling, so lets see.
        for 1 step we can only do [1] = 1
        for 2 steps we can do [1,1] or [2] = 2
        for 3 steps we can do [1,1,1] or [2,1] or [1, 2] = 3
        for 4 steps we can do [1,1,1,1] or [2,1,1] or [1,2,1] or [1,1,2] or [2,2] = 5
        the progression as can be seen here is 1, 2, 3, 5, 8 which is the fibonnaci sequence
        so lets implement the fib
        '''
        if n <= 2:
            # for 1 and 2 it is the same as n
            return n

        secondlast = 1
        last = 2
        for i in range(3, n + 1):
            current = secondlast + last
            secondlast = last
            last = current
        return last



       