from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = float('inf')
        min_sub = (0, 0)
        dict_t = Counter(t)
        sub_length = len(dict_t)
        formed_length = 0
        dict_s = {}       
        left = 0

        for right, char  in enumerate(s):
            dict_s[char] = dict_s.get(char, 0) + 1

            if char in dict_t and dict_t[char] == dict_s[char]:
                formed_length += 1

            while left <= right and formed_length == sub_length:
                curr_left = s[left]
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_sub = left, right

                dict_s[curr_left] -= 1
                if s[left] in dict_t and dict_s[curr_left] < dict_t[curr_left]:
                    formed_length -= 1
                
                left += 1
        
        return "" if min_length == float("inf") else s[min_sub[0]: min_sub[1]+1]
      
