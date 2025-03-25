class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using a set for O(1) look up in the nums array, convert the nums to a set for faster search
        checker = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in checker: # this means this is the start of the sequence
                temp = num
                local_longest = 1
                while temp + 1 in nums:
                    local_longest += 1
                    temp = temp + 1
                longest = max(longest, local_longest)
        return longest


    