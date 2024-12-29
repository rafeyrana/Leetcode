class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = collections.Counter(hand)
        hand.sort()
        # now for each num we are going to check if we can form the straight hand groups from it 
        # if we cannot then we are going to return False
        for num in hand:
            if counts[num]:
                for i in range(num, num + groupSize):
                    if not counts[i]:
                        return False
                    counts[i] -= 1
        return True
        