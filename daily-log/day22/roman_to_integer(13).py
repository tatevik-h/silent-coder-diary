class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
        }
        prev_value = 0
        prev = 0
        total = 0
        for char in s:
            value = roman[char]
            if prev_value < value:
                total = total - (2*prev_value) + value
            else:
                total = total + value
            prev_value = roman[char]
        return total
      
