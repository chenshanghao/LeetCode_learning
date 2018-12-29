"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        if n <= 0:
            return -1
        cad_index = 0
        
        for i in range(1, n):
            if Celebrity.knows(cad_index, i):
                cad_index = i
            
        for i in range(n):
            if i != cad_index and (Celebrity.knows(cad_index, i) == True or Celebrity.knows(i, cad_index)==False):
                return -1
        return cad_index
            
            