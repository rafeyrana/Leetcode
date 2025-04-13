class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we will try to shrink the window on the minimum element until the pivot is the minimum element
        # this requires us to move the pointers such that they move towards the side with the minimum element until both l and r pointers converge on it
        l, r = 0 , len(nums) - 1
        while l < r: # dont want them to overlap as they will overlap at the min
            m = l + (r - l ) // 2
            if nums[m] < nums[r]: # this means that the right side is sorted and the min is on the other side even if the array is rotated or not
                r = m
            else:
                l = m + 1
        # at the end of the loop l and r will be equal and will have converged on the minimum so we can return either of them
        return nums[r] # this can also be nums[l] because they are the same

        