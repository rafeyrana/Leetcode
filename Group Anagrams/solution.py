from collections import Counter
class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        for i , str_i in enumerate(strs):
            count = [0] * 26
            for char in str_i :
                count[ord(char) - ord("a")] += 1
            group_dict[tuple(count)].append(str_i)

            
        return (group_dict.values())
        