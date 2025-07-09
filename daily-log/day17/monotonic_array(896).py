class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = True
        isDecreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                isIncreasing = False
            elif nums[i] < nums[i + 1]:
                isDecreasing = False

        return isIncreasing or isDecreasing
      
