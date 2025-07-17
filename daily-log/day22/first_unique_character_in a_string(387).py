class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = []
        for char in set(s):
            if s.count(char) == 1:
                l.append(s.index(char))
        if len(l) > 0:
            return min(l)
        else:
            return -1
        
