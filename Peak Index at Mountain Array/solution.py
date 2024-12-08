class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        '''
        using binary search to go over the array, we know that before the peak it will be mid [i] > mid[i + 1] and after the peak it will be mid[i] < mid[i + 1]
        so we will use this to find the peak where the condition is reversed, when they both become equal we can escape and be done with it 
        
        '''
        r = len(arr)
        l = 0
        while l < r:
            mid = l + (r - l) // 2
            if mid + 1 < len(arr) and arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l

        