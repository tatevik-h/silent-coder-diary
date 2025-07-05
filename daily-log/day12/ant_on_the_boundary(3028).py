class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        pos = 0

        for move in nums:
            pos += move
            if pos == 0:
                count += 1

        return count
      
