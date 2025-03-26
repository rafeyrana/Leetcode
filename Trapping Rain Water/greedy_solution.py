class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        to determine the amount of water stored at each point we would need to check the difference between the current height and the last encountered max_height
        we can update the max_height when we encounter a height greater than the last height we had
        how do we find if it is contained or not hm
        water at each index is the min(max_height[l],max_height[r]) - height[i]
       
       1. Solution 1: greedy + precomputing: since we know that we will need the max height we have gotten so far from both sides and their mins
       we can get those from both sides, store them in arrays before and then get the total using the formula we have identified
        '''
        def left_maxes(arr):
            res = [0] * len(arr)
            max_l = arr[0]
            res[0] = max_l
            for i in range(1, len(arr)):
                max_l = max(max_l, arr[i])
                res[i] = max_l
            return res

        def right_maxes(arr):
            res = [0] * len(arr)
            max_r = arr[-1]
            res[-1] = max_r
            for i in range(len(arr) - 2, -1, -1):
                max_r = max(max_r, arr[i])
                res[i] = max_r
            return res

        max_heights_left = left_maxes(height)
        max_heights_right = right_maxes(height)
        max_water = 0
        for i in range(len(height)):
            max_water += min(max_heights_left[i], max_heights_right[i]) - height[i]
        return max_water

        