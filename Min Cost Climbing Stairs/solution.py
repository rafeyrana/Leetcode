class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        this is similar to the fibonnaci problem but here the intuition is for a cost as well, calculate the cost till the last step and then return the min of the last and second last step
        '''

        # since we can start from 0 or 1 index the cost to both is 0
        second_last = 0
        last = 0
        for i in range(len(cost)):
            c = cost[i] + min(second_last, last)
            second_last = last
            last = c
        # since we have to get to the last step that is beyond the list
        # get the min of the cost from the second last and last step
        c = min(second_last, last)
        return c
        