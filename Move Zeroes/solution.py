class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use a two pointer approach move the right one forward and if you find a n, swap it with the left one and increment the left one
        l , r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                # swap the l and r
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        return nums
        
            


        