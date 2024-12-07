class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        options = [i for i in range(1, 10)]
        def backtracking(path, opts, running_sum):
            if running_sum == n:
                if len(path) == k:
                    results.append(list(path))
                    return
                else:
                    return
            
            # but if it is greater we cant go forward
            if running_sum > n:
                return

            if not opts:
                return
            path.append(opts[0])
            backtracking(path, list(opts[1:]), running_sum + opts[0]) # in this we use the number 
            path.pop()
            backtracking(path, list(opts[1:]), running_sum) # in this case we dont use the number

        backtracking([], options, 0)
        return results

        