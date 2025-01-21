class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        we will use the simple approach of iterating through the array, adding the elements to the list and decreasing the bounds as we go
        '''
        l , r = 0 , len(matrix[0]) # not -1 because we need it to be outside the range as range is non inclusive of this
        top, bottom = 0, len(matrix)
        results = []
        
        # now we can keep decreaing them until the l and r not the same
        while l < r and top < bottom:
            # first we will get the top array
            results.extend(matrix[top][l : r])
            # since we have the top row now we will never come back to it so we can move the top pointer one down
            top += 1
            
            # now we have to get the elements on the right border
            for i in range(top, bottom):
                results.append(matrix[i][r - 1])
            # now we have the right boundary done as well so we can move that inwards as well
            r -= 1
            if not (l < r and top < bottom):
                break

            # now we are the bottom row which has to be added in reverse
            results.extend(matrix[bottom - 1][l : r][::-1]) 
            # now that we have gotten the bottom row we can move the bottom up as well
            bottom -= 1

            # now we need to get the left edge in reverse as well
            for i in range(bottom - 1, top - 1, -1):
                results.append(matrix[i][l])
            # move left forward
            l += 1

        return results



        