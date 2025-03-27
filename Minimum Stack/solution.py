class MinStack:
    '''
    using two stacks:
    1. One for the value that we have to add to the stack
    2. Min stack for keeping track of the minimum value uptil this point
    performs all operations in O(1)
    
    '''

    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
