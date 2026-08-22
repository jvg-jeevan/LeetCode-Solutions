class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        digit_sum = 0
        digit_product = 1

        while n > 0:
            rem = n % 10
            digit_sum += rem
            digit_product *= rem 
            n //= 10

        print(digit_sum, digit_product)
        
        return original % (digit_sum + digit_product) == 0