class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        r = 1
        max_len = 0
        counter = 1 if word[0] == 'a' else 0
        l = 0

        while r < len(word):
            if  word[r] < word[r-1]:
                l = r
                counter = 1 if word[r] == 'a' else 0
            elif word[r] > word[r-1] :
                counter += 1

            if counter == 5:
                max_len = max(max_len, r-l +1)
            r += 1

        return max_len
      
