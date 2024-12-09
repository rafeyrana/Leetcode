class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # since we can have both the negative numbers and the positive numbers as well as 0 we need to keep a track of the minimum product sum as well in case it is multipled with a neg value found in the future
        # also keep in mind that since we are looking for the subarray this can also mean a single element itself which can be the subarray of size 1
        # so we can keep the most min value and the most max value, if the currMin value turns into a positive value, it will be changed to the maxProduct on the next turn
        # starting with the first element / subarray
        currMax = nums[0]
        currMin = nums[0]
        maxProduct = nums[0]
        for num in nums[1:]:
            currMax, currMin = max(num, num * currMax, num * currMin), min(num, num * currMax, num * currMin)
            maxProduct = max(maxProduct, currMax)
        return maxProduct

        