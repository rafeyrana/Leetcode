class TimeMap:
    def __init__(self):
        self.time_map = {} # the key will be the key and the values will be a list in which we add the items at the end

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map or self.time_map[key] == []:
            return ""
        # if the key exists since they have been added in the list for that key in increasing order we can look for it using the binary search
        search = self.time_map[key]
        l , r = 0, len(search) - 1
        result = ""
        while l <= r:
            mid = l + (r - l) // 2
            if search[mid][1] == timestamp:
                return search[mid][0]
            elif search[mid][1] < timestamp:
                result = search[mid][0]  # this is a valid candidate
                l = mid + 1  # look for better candidates in the right half
            else:
                r = mid - 1  # mid is too high
        return result
        
        
