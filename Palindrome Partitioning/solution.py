class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        self intuition:
        the idea here is that the string can be split into multiple partitions, as many as you like and we can check if each of those is a palindrome or not. for each type of partition we will check all the combinations for a palindrome and add them to a results array when we reach the end of the array
        we can use backtracking to check all the combinations of partitions
        the inner for loop is going to check for all inner commbinations of the string being palindomes, if they are a palindome we will save it and add a partition there and have the algo try more options in the future of this part of the string
        
        
        
        
        
        gpt explanation:

        he solution to the problem leverages backtracking (DFS) to explore all possible ways to partition the input string s into palindromic substrings. It starts by iterating through the string and at each index, attempts to create a substring. For each substring, it checks if it is a palindrome using a helper function is_palindrome that compares characters from both ends. If the substring is a palindrome, it is added to the current partition, and the algorithm recursively explores further partitions from the next index. Once the end of the string is reached, the current partition is stored as a valid result. The algorithm backtracks by removing the last added palindrome substring and continues exploring other potential palindromic partitions. This process continues until all possible palindromic partitions are found.
        '''
        results = []

        def isPalindrome(string):
            # Check if a string is a palindrome using two pointers
            i, j = 0, len(string) - 1
            while i <= j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtracking(start_idx, current_partition):
            # If we've reached the end of the string, add the partition to results
            if start_idx == len(s):
                results.append(current_partition[:])  # Append a copy of the current partition
                return

            # Explore all possible substrings starting from start_idx
            for end_idx in range(start_idx, len(s)):
                substring = s[start_idx:end_idx + 1]

                # Check if the current substring is a palindrome
                if isPalindrome(substring):
                    # Choose: Add the substring to the current partition
                    current_partition.append(substring)

                    # Explore: Recur for the remaining substring
                    backtracking(end_idx + 1, current_partition)

                    # Unchoose: Backtrack by removing the last added substring
                    current_partition.pop()

        # Start backtracking from the beginning of the string
        backtracking(0, [])
        return results
