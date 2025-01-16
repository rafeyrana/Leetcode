class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        the trick to this question is a sliding window
        we will start by keeping a hashmap of the t string which we will need to keep a track of
        then we can iterate through the whole array using l and right pointers and whenever we satisfy the condition of having all the characters from t in the window
        we will note down its length and indices, then we will move the left pointer forward until we can remove one of the characters in t from the list to keep continuning finding the shortest one
        
        '''
        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)  # Initialize the hashmap for `t`
        
        have, need = 0, len(countT)
        results, resultLength = [-1, -1], float('inf')
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # Does this count satisfy the condition?
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # Contract the window from the left while valid
            while have == need:
                # Update the result if this window is smaller
                if r - l + 1 < resultLength:
                    resultLength = r - l + 1
                    results = [l, r]
                
                # Pop from the left of the window and make it smaller
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1  # Move the pointer forward
        
        l, r = results
        return s[l:r + 1] if resultLength != float('inf') else ""
