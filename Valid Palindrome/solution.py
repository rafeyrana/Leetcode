class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first we need to clean the string to keep only the alphanumeric characters
        # then we can use a two pointer approach to check the characters on both sides for this
        def clean_string(s : str) -> str:
            res = ""
            for char in s:
                if "A" <= char <= "Z" or "a" <= char <= "z" or "0" <= char <= "9":
                    res += char.lower()
            return res
        cleaned_string = clean_string(s)
        # now that we have the cleaned string we can move on to checking if its a palindrome
        # being a palindrome means that characters at the same index from opposite sides should be the same
        # this calls for a two pointer approach
        l , r = 0 , len(cleaned_string) - 1
        while l < r:
            if cleaned_string[l] != cleaned_string[r]:
                return False
            l += 1
            r -= 1
        return True