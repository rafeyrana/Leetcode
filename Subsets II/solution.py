
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()  
        iterations = len(nums)

        def backtracking(index, sol):
            if index == iterations:
                results.append(sol[:])
                return
            
            # Include the current element
            sol.append(nums[index])
            backtracking(index + 1, sol)
            sol.pop() # go back on that

            # Skip duplicates
            while index + 1 < iterations and nums[index] == nums[index + 1]:
                index += 1

            # Do not include the current element
            backtracking(index + 1, sol)

        backtracking(0, [])
        return results
