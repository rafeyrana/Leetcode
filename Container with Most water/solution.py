class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        1. what does amount of water mean here? is it the area?
            how do we calculate the area? index diff of the two bars and the min of their heights?



        the brute force approach is to check each and every pair given here to check which of them is the largest in terms of the areas
        or we can use a two pointer approach because we are exploring a linear structure and need to optimise for the largest area
        so the two pointers will start at opposite sides and then converge towards the middle
        but how do we move the pointers until they cross
        since the bounding factor for the area calculation is the min of the heights we need to change that to get a better area so we will move the element with the smaller height 
        '''
        left_pointer = 0 
        right_pointer = len(heights) - 1
        max_water_area = 0
        
        while left_pointer < right_pointer:
            current_area = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)
            max_water_area = max(current_area, max_water_area)
            
            if heights[left_pointer] > heights[right_pointer]:
                right_pointer -= 1
            else:
                # if less than or equal so we choose to move the left pointer if they are equal
                left_pointer += 1
                
        return max_water_area
        