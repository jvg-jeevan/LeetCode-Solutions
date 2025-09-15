class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        res = 0
        for word in text:
            canType = True
            for letter in word:
                if letter in brokenLetters:
                    canType = False
                    break
            if canType:
                res += 1

        return res