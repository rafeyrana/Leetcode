class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # so to find this we can use a two pointer approach
        # use a dict to keep a track of the index of each element, if not in the dict move the right pointer forward by 1, if in dict update the index by adding this one and moving left forward by one
        left = 0
        right = 0
        chars = {}
        max_length = 0
        length_of_string = len(s)
        while right < length_of_string:
            if s[right] in chars and chars[s[right]] >= left:
                # Move the left pointer to the position after the last occurrence of s[right].
                left = chars[s[right]] + 1
                
            chars[s[right]] = right
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length