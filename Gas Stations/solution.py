class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        i dont understand the neetcode solution for this so i am going to my most optimised naive solution
        we have to iterate over all the nodes and figure out if we can make it back to the node that we started at
        the way to iterate over a circular array is using the mod of the length of the array to give you the index back, this will be an O(n**2) solution but we will make some optimisations along the way
        these will be to check if the gas is enough for a round trip or not and not continuing to the next index if the total is negative at any point
        '''
        if sum(gas) < sum(cost):
            return -1
        res = 0
        total_elements = len(gas)
        while res < total_elements:
            total = 0
            for i in range(res, total_elements + res + 1):
                idx = i % total_elements
                total += (gas[idx] - cost[idx])
                if total < 0:
                    break
            if total >= 0:
                return res
            res += 1
        
                
        
