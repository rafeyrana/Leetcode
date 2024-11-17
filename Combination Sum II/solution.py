class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # similar solution as the combination sum and duplicate subsets, essentially you sort in advance, keep the same checks as the combination sum which is for returnng if you exceed and adding to solutions if equal to the target sum
        iterations = len(candidates)
        candidates.sort()
        results = [] # store all combinations
        # running sum as we go
        def backtracking(i , sol, sol_sum):
            # if equal
            if sol_sum == target:
                results.append(sol[:])
                return
            # if not equal and more than the sum or the list is finished
            if sol_sum > target or i >= iterations:
                return
            
            # now the real fun begins, send the current index by adding it and call the backtrack funciton
            sol.append(candidates[i])
            backtracking(i + 1, sol, sol_sum + candidates[i])
            
            sol.pop()
            while i + 1 < iterations and candidates[i] == candidates[i + 1]:
                i+=1
            backtracking(i + 1, sol, sol_sum)

        backtracking(0, [], 0)
        return results

            
            