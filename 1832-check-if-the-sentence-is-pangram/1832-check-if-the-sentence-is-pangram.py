class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # to check take res with all false
        res = [False] * 26
        for i in sentence:
            res[ord(i)-97] = True
        # if all characters are found then all true and return true
        return all(res)