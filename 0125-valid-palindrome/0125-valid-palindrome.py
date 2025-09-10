class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    new_str += i.lower()
                else:
                    new_str += i

        print(new_str)
        print(new_str[::-1])
        
        return new_str == new_str[::-1]