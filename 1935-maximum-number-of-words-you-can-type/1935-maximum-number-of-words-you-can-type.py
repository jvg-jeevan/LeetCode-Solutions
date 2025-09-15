class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        res = 0
        # iterate through each word
        for word in text:
            # canType to check whether
            canType = True
            for letter in word:
                # if letter is in given its false and exit of loop
                if letter in brokenLetters:
                    canType = False
                    break
            # check if canType and increment result
            if canType:
                res += 1

        return res