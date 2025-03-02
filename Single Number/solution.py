class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # one easy way to do this is to use a set, add if this is the first time we have seen it else we will remove it
        # at the end only the number that has not been seen more than once it will be remaining in there
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         seen.remove(num)
        #     else:
        #         seen.add(num)
        # return list(seen)[0]


        # using bit manipulation
        # represent the numbers in their bits and take their xor with 
        # if the bits are the same they become 0 and if different we get 1
        # so if we take the xor of all the numbers here we will get the number that is not duplicated
        # the order doesnt matter here
        # 0s in every XOR always means 0 so we can ignore them
        # if have an even number of 1s then we get 0 else it will be 1, since we have duplicates it will always be 0


        res = 0
        for num in nums:
            res = num ^ res
        return res

        