class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        think of this in reverse, starting from the last index which will be the initial goal. in. areverse loop fi the goal can be reached by the i + nums[i] then that means that the goal is to now get to that index after which we are sure we will get to the end, change the goal to that index, in the end check if the goal has reached 0 which means it is reachable else it is not
        '''
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal: # if we can reach the goal we shift that goal to the goal being the i being reachable from other indexes
                goal = i
        return goal == 0
        
        