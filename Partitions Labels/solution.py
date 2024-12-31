from typing import List

class Solution:
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
