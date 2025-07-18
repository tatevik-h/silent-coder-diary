class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_count = 0
        count_map = {0: -1}
        count = 0

        for i, elem in enumerate(nums):
            count += 1 if elem == 1 else -1
            if count in count_map:
                max_count = max(max_count, i - count_map[count])
            else:
                count_map[count] = i

        return max_count
      
