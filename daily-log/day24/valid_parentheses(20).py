class Solution:
    def isValid(self, s: str) -> bool:
        parentheses= {'}': '{', ']': '[', ')': '('}
        stack = []
        for char in s:
            if char in parentheses.values():
                stack.append(char)
            elif char in parentheses: 
                if not stack or stack[-1] != parentheses[char]:
                    return False
                stack.pop()
            else:
                return False


        return not stack
      
