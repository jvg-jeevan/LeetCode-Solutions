class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        num = 0
        if x < 0:
            return False
        
        while x > 0:
            num = (num * 10) + (x % 10)
            x //= 10
        return num == temp