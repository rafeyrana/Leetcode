class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # this can be solved using a dp approach, we will keep a set in which we will add every single element with the previous sums and keep going until we find the target which in our case will be sum(nums) // 2
        s_nums = sum(nums)
        if s_nums % 2 == 1:
            return False
        target = s_nums // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            set_copy = set(dp)
            for t in set_copy:
                s = nums[i] + t
                if s == target:
                    return True
                dp.add(s)
        return False