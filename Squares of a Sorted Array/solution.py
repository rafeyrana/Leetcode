class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # since we know that the squares on both ends will be the max as this is a non decreasing array, we can use the principle of two pointers until they meet
        results = [0] * len(nums)
        start = 0
        end = len(nums) - 1
        counter = len(nums) - 1
        while start <= end:
            if abs(nums[start]) >= abs(nums[end]):
                results[counter] = nums[start] ** 2
                start += 1
            else:
                results[counter] = nums[end] ** 2
                end -= 1
            counter -= 1

        return results
                

