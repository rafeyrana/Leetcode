from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        our_target = [0, 0, 0]

        # Process each triplet
        for triplet in triplets:
            # Skip triplets that exceed any element of the target
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            # Update our_target with the maximum values from valid triplets
            for idx in range(3):
                our_target[idx] = max(our_target[idx], triplet[idx])

        # Check if we can match the target
        return our_target == target
