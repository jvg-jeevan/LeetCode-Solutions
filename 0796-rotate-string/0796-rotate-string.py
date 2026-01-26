class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # concatenate s string twice if rotated you find goal in it
        if len(s) != len(goal):
            return False
        temp = s+s
        return temp.find(goal) != -1