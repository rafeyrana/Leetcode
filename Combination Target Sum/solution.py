class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # okay so the tip here is to find all the combinations we can go down two paths, one is to include the current element and then have the decision to include it or not in the followinf recursive call
        # and one is to not include it and go down the path where it does not exist to explore all other combinations
        # this is a combinations question not a permutations one that is why we cannot have doubles
        results = []
        # we will use the index to keep a track of the element being added or not
        sol = []

        def backtracking(i):
            sum_sol = sum(sol)
            if sum_sol == target:
                results.append(sol[:])
                return
            if sum_sol > target or i >= len(nums):
                return
            # now the two options
            # add and send with the same options or dont add and skip entirely
            sol.append(nums[i])
            backtracking(i)
            sol.pop()
            backtracking(i + 1)
        backtracking(0)
        return results

