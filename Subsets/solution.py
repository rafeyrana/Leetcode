class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        when we have to explore the whole space and return all solutions we can use a backtracking approach
        now we have no constaints here except that we have to go three steps
        at each step we have the option to keep or not keep a value
        '''
        results = []
        sol = []
        n = len(nums)

        # i is the index in this case of the element in the list
        def backtrack(i):
            if i == n:
                results.append(sol[:])
                return
             # now we have two choices to make , one we can call this without including it in the solution
            backtrack(i + 1)
            # or we can add it and call it
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop(-1)
        backtrack(0)
        return results
