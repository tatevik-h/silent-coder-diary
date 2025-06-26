class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        left = 0
        length = len(s)
        max_length = 0
        for right in range(length):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            
            seen_chars.add(s[right])
            max_length = max(max_length, right - left + 1)
                
        return max_length
