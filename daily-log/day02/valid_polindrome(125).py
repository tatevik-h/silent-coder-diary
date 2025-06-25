class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        left, right = 0, len(clean_s) - 1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1

        return True
