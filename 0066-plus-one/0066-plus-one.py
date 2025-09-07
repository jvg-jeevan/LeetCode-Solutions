class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        result = []
        # get list items in number
        for i in digits:
            num = (num*10) + i

        # add 1 
        num += 1

        # get the remainder and start adding at the 0th position
        # so that last digit is msb
        while num > 0:
            result.insert(0, num % 10)
            num //= 10
        
        return result