class MinStack:
    '''
    using two stacks:
    1. One for the value that we have to add to the stack
    2. Min stack for keeping track of the minimum value uptil this point
    performs all operations in O(1)
    only add to the min stack if it is smaller than the last min or else no point in adding as it is not going to be a min
    
    '''

    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        val = self.main_stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
