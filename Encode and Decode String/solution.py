class Solution:
    # we will need to implement a unique way to store the numbers and their lengths
    # does this contain numbers?
    # use a delimiter that is relatively rare and not usually so important that it can be overlooked in real life production systems
    # we will use the rarest character i can find coupled with the length of the word to make sure that the string is properly decoded
    # the char we are using is : 𓀴 which is an egyptian hyroglyphic
    # the string will look something like 1𓀴i2𓀴am3𓀴rafey
    # each word can be more than a 10 characters long so finding a single int wont be enough in this case
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "𓀴" + word
        return encoded_string

        

    def decode(self, s: str) -> List[str]:
        result = []
        if not s or len(s) < 3:
            return result
        l = 0 
        while l < len(s):
            size = ""
            while s[l] != "𓀴":
                size += s[l]
                l += l
            print(size)
            size_int = int(size)
            l += 1
            word = s[l : l + size_int]
            result.append(word)
            l += size_int
        return result
    