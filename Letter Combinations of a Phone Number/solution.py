class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []

        num_mapping = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]
        }

        def backtracking(sol, i):
            if len(sol) == len(digits):
                if sol:
                    results.append("".join(sol))
                return

            # if not it we can do that go over all the options for this use case and then move to the next index

            for num in num_mapping[int(digits[i])]:
                sol.append(num)
                backtracking(sol, i + 1)
                sol.pop()

        backtracking([], 0)
        return results

        