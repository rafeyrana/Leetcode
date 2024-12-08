class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        r = len(arr)
        l = 0
        while l < r:
            mid = l + (r - l) // 2
            if mid + 1 < len(arr) and arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l

        