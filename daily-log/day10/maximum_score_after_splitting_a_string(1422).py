class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        left_score = 0
        right_score = s.count('1')
        for i in range(len(s)-1):
            if s[i] == '0':
                left_score += 1
            else:
                right_score -= 1

            max_score = max(max_score, left_score + right_score)

        return max_score

