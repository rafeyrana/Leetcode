class NumArray:
    '''
    this is a simple prefix sum problem which will just use a one directional prefix summed array to give the sum of the elements between left and right inclusive
    '''

    def __init__(self, nums: List[int]):
        self.len_array = len(nums)

        def build_array():
            prefix_sum = [0] * (self.len_array + 1)
            total = 0
            for i in range(self.len_array):
                total += nums[i]
                prefix_sum[i + 1] = total
            return prefix_sum

        self.prefix_sum = build_array()
        
    
    def sumRange(self, left: int, right: int) -> int:
        return (self.prefix_sum[right + 1] - self.prefix_sum[left])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)