class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        l , r = 0 , len(nums) - 1
        while l <= r:
            mid = l + (r - l ) // 2 # accounting for overflow in large arrays
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return - 1

        