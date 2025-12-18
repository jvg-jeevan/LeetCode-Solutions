class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1
                late = 0
            elif s[i] == 'L':
                late += 1
                if late >= 3:
                    return False
        return True if absent < 2 else False