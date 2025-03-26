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
        # def left_maxes(arr):
        #     res = [0] * len(arr)
        #     max_l = arr[0]
        #     res[0] = max_l
        #     for i in range(1, len(arr)):
        #         max_l = max(max_l, arr[i])
        #         res[i] = max_l
        #     return res

        # def right_maxes(arr):
        #     res = [0] * len(arr)
        #     max_r = arr[-1]
        #     res[-1] = max_r
        #     for i in range(len(arr) - 2, -1, -1):
        #         max_r = max(max_r, arr[i])
        #         res[i] = max_r
        #     return res

        # max_heights_left = left_maxes(height)
        # max_heights_right = right_maxes(height)
        # max_water = 0
        # for i in range(len(height)):
        #     max_water += min(max_heights_left[i], max_heights_right[i]) - height[i]
        # return max_water

        '''
        2. Solution 2: use a left and right pointer and keep track of the max_left and the max_right
        at each step which ever side is shorter will move inwards, update the max or wtv and keep going until they cross
        now the way to figure out when to move the pointer because the water is not trapped and when the water is trapped is dependant on the current height at that index in comparison to the max on that side
        '''
        l ,r = 0 , len(height) - 1
        left_max , right_max, total_water = 0,0,0
        while l < r:
            if height[l] < height[r]: # whichever side is smaller is the bounding factor for the amount of water we can store
                if height[l] >= left_max: # we cannot store any water here as this is the new boundary / left _max
                    left_max = height[l]
                else: # if this is not the boundary then this will have some amount of water being trapped here
                    total_water += left_max - height[l] 
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    total_water += right_max - height[r]
                r -= 1
        return total_water