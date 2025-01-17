class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # first lets do the naive solution
        start_counter = 0
        end_counter = len(heights) -1
        max_area= 0
        while start_counter != end_counter and start_counter < len(heights) :
            print(start_counter, end_counter)
            area = min(heights[start_counter], heights[end_counter]) * abs(start_counter - end_counter)
            if area > max_area:
                max_area = area 
            if heights[start_counter] < heights[end_counter]:
                start_counter += 1
            elif heights[start_counter] > heights[end_counter]:
                end_counter -= 1
            else:
                start_counter += 1
                end_counter -= 1

        return max_area
        