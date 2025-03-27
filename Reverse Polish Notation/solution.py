class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # using a stack to store numbers until we encounter an operand
        # pop last two values and perform the operation and push the result back on to the stack until we are donw
        # assume this will always be valid and will always evaluate to one single solution which we can return
        stack = []
        for token in tokens:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    first_pop = stack.pop()
                    second_pop = stack.pop()
                    stack.append(second_pop - first_pop)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    first_pop = stack.pop()
                    second_pop = stack.pop()
                    stack.append(int(second_pop / first_pop))
                case _:
                    stack.append(int(token))
        return stack[-1]

                
        