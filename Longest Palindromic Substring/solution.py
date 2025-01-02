class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Optimized approach:
        Use a 2D dp table where dp[start][end] indicates whether the substring s[start:end+1] is a palindrome.
        '''
        n = len(s)
        # Step 1: Create a 2D DP table initialized with False
        dp = [[False] * n for _ in range(n)]
        longest, longest_pali = 0, ""

        for end in range(n):
            for start in range(end + 1):
                # Check if the substring s[start:end+1] is a palindrome
                if s[start] == s[end]:
                    # A single character or two consecutive matching characters are palindromes
                    if end - start + 1 <= 2: 
                        dp[start][end] = True
                    else:
                        # For longer substrings, check if the inner substring is a palindrome
                        dp[start][end] = dp[start + 1][end - 1]
                    
                # If it is a palindrome, check if it's the longest so far
                if dp[start][end] and end - start + 1 > longest:
                    longest = end - start + 1
                    longest_pali = s[start:end + 1]
        
        return longest_pali
