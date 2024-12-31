class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        the intuition is to go over the string in one pass. we will keep a track of the possible values of the open paranethesis count using the min and max algo such as the * will either change it by -1, 0, +1 and then we can maintain the range
        if the value ever goes to -1 we will not keep it and we will make it 0
        check for another case that if the max_open is ever less than 0 then the order is not correct and we have to return false for this
        in the end if the min is zero that means that at some point while iterating and considering all possible combos they combined to sum up to 0 meaning the string has been balanced
        '''
        min_open = max_open = 0
        for c in s:
            if c == "(":
                min_open += 1
                max_open += 1
            elif c == ")":
                min_open -= 1
                max_open -= 1
            else:
                min_open = min_open - 1 # in this case the minimum value can be in the case of it being )
                max_open = max_open + 1
            if min_open < 0:
                min_open = 0
            if max_open < 0:
                return False
        # now that we have traversed the whole array we can check if at any point we had that balanced or not
        return min_open == 0

        