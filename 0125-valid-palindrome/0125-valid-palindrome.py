class Solution:
    def isPalindrome(self, s: str) -> bool:
        # take new_str to take only alpha and num chars
        new_str = ""
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    new_str += i.lower()
                else:
                    new_str += i

        print(new_str)
        print(new_str[::-1])

        # compare with original 
        return new_str == new_str[::-1]