class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for k in nums:
            length = 0
            if k - 1 not in nums_set:
                length += 1
                while k + length in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest
                