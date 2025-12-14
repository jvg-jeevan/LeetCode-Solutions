class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high + 1) // 2) - (low//2)
        # odds in [low,high] = odds(high)−odds(low−1)
        # odds(x)=⌊(x+1)/2​⌋