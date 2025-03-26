class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        this is similar to the two sum but since we cannot do any better than having to go over all the elements atleast twice we can 
        make our approach easier by first sorting the array and for each index use a sorted two sum approach using a sliding window there
        since we need to add up to 0 the inner two pointer will have to find the neg value of the main upper variable that we are using as our first value
        '''
        nums = sorted(nums)
        results = []
        array_length = len(nums)
        first_idx = 0
        
        while first_idx < array_length:
            # Skip duplicates for the first number
            if first_idx > 0 and nums[first_idx] == nums[first_idx - 1]:
                first_idx += 1
                continue
                
            target_sum = -nums[first_idx]
            left_idx, right_idx = first_idx + 1, array_length - 1
            
            while left_idx < right_idx:
                if nums[left_idx] + nums[right_idx] == target_sum: 
                    results.append([nums[first_idx], nums[left_idx], nums[right_idx]])
                    left_idx += 1
                    right_idx -= 1
                    
                    # Skip duplicates for second number
                    while left_idx < right_idx and nums[left_idx] == nums[left_idx - 1]:
                        left_idx += 1
                    # Skip duplicates for third number
                    while left_idx < right_idx and nums[right_idx] == nums[right_idx + 1]:
                        right_idx -= 1
                        
                elif nums[left_idx] + nums[right_idx] < target_sum:
                    left_idx += 1
                else: 
                    right_idx -= 1
                    
            first_idx += 1
            
        return results
        
                
                

        