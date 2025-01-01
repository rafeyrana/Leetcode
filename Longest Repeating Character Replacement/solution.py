class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use a dictionary to keep a track of the number of times any character is seen in the sliding window.
        # maintain a variable to keep a track of the max frequency of the elements in the sliding window which gives us the total number of elements in the array
        # change the left and right pointers based on this
        length = len(s)
        count = {}
        longest = 0
        maxi_f = 0
        l = 0
        for r in range(length):
            count[s[r]] = count.get(s[r],0) + 1 # seen this element one more time
            maxi_f = max(maxi_f, count[s[r]]) # check if this has occured the most


            # now lets check if it has exceeded the limit
            if (r - l + 1 - maxi_f > k): 
                count[s[l]] -= 1
                l += 1
            longest = max(longest ,r - l + 1 )
        return longest