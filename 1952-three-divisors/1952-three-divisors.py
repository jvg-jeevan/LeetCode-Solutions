from math import ceil
class Solution:
    def isThree(self, n: int) -> bool:
        # only the square of the prime numbers have 3 divisors
        # check if sqrt(num) is prime number


        num = int(n**0.5)
        if num * num != n:
            return False

        if n <= 3:
            return False

        i = 2
        while i*i <= num:
            if num%i == 0:
                return False
            i += 1
        
        return True