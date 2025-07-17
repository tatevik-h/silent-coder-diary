class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_c = Counter(s)
        for elem in t:
            if elem  in s_c and s_c[elem] > 0:
                s_c[elem] -= 1
            else:
                return elem
            
