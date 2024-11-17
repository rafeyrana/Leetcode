from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtracking(arr, numbers):
            if len(arr) == len(nums):
                results.append(arr[:]) 
                return

            for num in numbers:
                arr.append(num)
                numbers_copy = numbers[:]
                numbers_copy.remove(num)
                backtracking(arr, numbers_copy)
                arr.pop()

        backtracking([], nums)
        return results
