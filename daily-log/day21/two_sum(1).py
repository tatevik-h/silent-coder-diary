class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_items = {}
        for i in range(len(nums)):
            if target - nums[i] in seen_items:
                return [i, seen_items.get(target-nums[i])]
            seen_items[nums[i]] = i
        return
      
