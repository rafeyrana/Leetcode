class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0: # since the array is sorted if the number is more than 0 we will not be finding the solution down the line as the numbers are going to be greater than 0
                break
            if i > 0 and nums[i] == nums[i - 1]: # duplicate case
                continue
            l , r = i + 1, len(nums) - 1
            while l < r:
                result = num + nums[l] + nums[r]
                if result == 0:
                    results.append([num, nums[l] ,nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif result > 0:
                    # since our array is sorted we need a smaller number
                    r -= 1
                elif result < 0 :
                    # we need a bigger number
                    l += 1
            
        return results