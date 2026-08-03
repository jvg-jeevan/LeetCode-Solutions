import math

class Solution:
    def numTrees(self, n: int) -> int:
        # using catalan number 
        return math.comb(2*n, n) // (n+1)