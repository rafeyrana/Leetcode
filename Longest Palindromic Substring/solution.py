class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        lets start with the most naive approach:
        1. function for checking palindrome
        2. if palindrome: update and store the longest palindrome found so far

        this will cause a time limit exceeded exception because we are rechecking the word strings over and over

        this can be optimised using a 1d dp approach using a hashmap with the substring as the key and the value as the if it is a palindrome
        '''
        def checkPalindrome(s):
            l , r = 0 , len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        n = len(s)
        dp = {}
        longest, longest_pali = 0, ""
        for start in range(n):
            for end in range(start, n):
                # this loop will ensure that we will go over every single sub array possible
                substring = s[start: end + 1]
                dp[substring] = dp.get(substring, checkPalindrome(substring))
                is_palindrome = dp[substring]
                if is_palindrome and end - start + 1 > longest:
                    longest = end - start + 1
                    longest_pali = s[start: end + 1]
        return longest_pali
                    
        