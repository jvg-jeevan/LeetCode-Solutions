class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def digitProduct(num):
            prod = 1
            while num > 0:
                prod = prod * (num % 10)
                num //= 10
            return prod            

        while True:
            if digitProduct(n) % t == 0:
                return n
            n = n + 1