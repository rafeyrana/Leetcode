from typing import List

class Solution:

    '''
    make a dict of the last idx of each character in the string. since the constraint is that each character cannot be in more than one substring so when we traverse the string using two pointers, the current character will be in the current substring and that will go up to atleast the last index of this character. so when we get a new character get a max of the end and the chars last index. after this check if the end is now equal to the current idx of the string we are at meaning that this is the last one then we append the end - start + 1 to the results string and move the start to this index + 1 to indicate the start of the next partition
    '''
    def partitionLabels(self, s: str) -> List[int]:
        # Keep track of the last occurrence of each character
        last_idx = {char: idx for idx, char in enumerate(s)}
        
        # Initialize pointers and results list
        start = 0
        end = 0
        results = []
        
        # Iterate through the string
        for idx, char in enumerate(s):
            # Update the end of the current partition
            end = max(end, last_idx[char])
            
            # If the current index matches the end of the partition
            if idx == end:
                # Append the size of the partition
                results.append(end - start + 1)
                # Update the start pointer for the next partition
                start = idx + 1
        
        return results
