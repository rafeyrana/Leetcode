class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ''' since we have to generate ALL solutions that are valid this seems like a backtracking + recursion problem
        for paranthesis of n to be valid they must have n opening and n closing paranthesis
        and for each valid but not yet ended combination the number of opening parentheses can be more than the closing
        but if closing is more then it is instantly invalid
        we can use a recursive approach here and try to build a string containing the paranthese recursively
        we should keep a track of the opening and closing bracket count and at each recursive step we can check if we can add an opening bracket and make the next call or add a closing bracket and make the next call to the recursive function
        when does the recursion end? the string length cannot exceed 2n because n number of parantheses means 2n chars
        if the length is 2n and the combo is valid until that point meaning the closing number == opening number we can consider it a valid solution
        '''
        results = []
        def backtracking(s, opening, closing):
            if len(s) == 2 * n:
                if opening == closing:
                    results.append(s)
                return
            # we can always add an opening bracket
            backtracking(s + "(", opening + 1, closing)
            # only add a closing bracket if it is less than or equal to the number of the opening brackets
            if opening > 0 and closing < opening:
                backtracking(s + ")", opening, closing + 1)
        backtracking("", 0, 0)
        return results