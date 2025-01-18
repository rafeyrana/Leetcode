class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # making a dict for keeping the diff as the key and the index as the value and iterating through it to find the diff value
        diff_dict = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in diff_dict:
                return [diff_dict[diff], idx]
            diff_dict[num] = idx
        
        