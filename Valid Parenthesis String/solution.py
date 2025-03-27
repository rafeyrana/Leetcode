class Solution:
    def isValid(self, s: str) -> bool:
        '''
        so if we have to go through the string of paranthesis going in order
        the last open paranthesis has to be the first to be closed and the second and then so on
        this points to Last In First Out Approach we will need to use a stack to keep a track of the opening brackets and when we encounter a closing bracket we pop from the stack and check if its the corresponding bracket or not
        early return False and return True at the end
        '''
        stack = []
        parans = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for char in s:
            if char not in parans:
                stack.append(char)
            elif not stack or stack.pop() != parans[char]:
                return False

        return not stack # stack should be empty
        