class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the most naive solution for this would be to take a product of every single element and then divide by the current element to get the solution
        # but this wont work if there are multiple 0s in the array
        # a prefix and suffix approach would be helpful here
        # prefix array
        if not nums:
            return []
        prefix = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        # at this point we have the product of all the elements before the current one in the array
        # we can now do this in reverse and make the same array
        postfix = 1
        for r in range(len(nums) - 1, -1 , -1):
            result[r] *= postfix
            postfix *= nums[r]

        return result

            