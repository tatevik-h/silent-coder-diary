class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52

        for start, end in ranges:
            diff[start] += 1
            diff[end + 1] -= 1

        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left<= i <= right and curr <= 0:
                return False

        return True
      
