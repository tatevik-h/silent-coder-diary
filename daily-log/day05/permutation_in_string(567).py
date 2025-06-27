from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length =len(s1)
        len_s2 = len(s2)
        dict_s1 = Counter(s1)

        for i in range(len_s2):
            left = i
            dict_s2 = Counter(s2[left: i+length])
                
            if dict_s1 == dict_s2:
                return True
        return False
      
