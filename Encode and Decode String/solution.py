class Solution:

    def encode(self, strs: List[str]) -> str:
        # using a number to denote the number of characters in the word with some sort of delimiter before we join them
        # so essentially that would be neet would become 4^neet , we will be suing rare charater that is not really used a lot to avoid a lot of confusion in encoding and decding
        final_str = ""
        for word in strs:
            final_str += str(len(word)) + "^"  + word
        return final_str


    def decode(self, s: str) -> List[str]:
        # now in the decode we can expect a string lke 4^neet4^code4^love3^you
        # we will iterate through the list, find the length until the delimiter, once we find the delimiter the  string which we will use with the current index and string indexing to remove and move the current pointer forward
        curr = 0
        result = []
        while curr < len(s):
                end_ptr = curr
                while s[end_ptr] != "^":
                    end_ptr += 1
            
                word_length = int(s[curr: end_ptr])
                curr = end_ptr + 1
                end_ptr = curr + word_length
                
                word = s[curr : end_ptr]
                result.append(word)
                curr = end_ptr
                
        return result
