class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ''' 
        since the array is sorted in non decreasing order we can be sure that the smaller elements will be on the left
        and the bigger ones will be on the right.

        we can use a two pointers approach here for finding the target
        add two numbers on the l and r pointers
        if the number is greater than the target that means we need to use a smaller number to add to it so move the r pointer by -1
        if the sum is less than the target that means we need to use a bigger number to add to it so move the l pointer by + 1
        when sum found check for the indexes being equal if they are equal we can deal with it
        '''
        l , r = 0 , len(numbers) - 1
        while l < r: # if they are the same we break and never let that happen
            if numbers[l] + numbers[r] == target:
                return [l + 1 , r + 1] # 1 indexed array
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
            # no need for final case because we are guaranteed a solution here
        
        