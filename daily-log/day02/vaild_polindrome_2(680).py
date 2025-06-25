class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                i, j = left + 1, right
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                
                if i >= j:
                    return True

                i, j = left, right - 1
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                
                if i >= j:
                    return True                

                return False
            
            else:
                left += 1
                right -= 1 
                
        return True
