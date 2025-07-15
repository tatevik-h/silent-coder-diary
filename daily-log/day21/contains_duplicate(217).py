class Solution0:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)
        for k, v in nums_count.items():
            if v >= 2:
                return True
            
        return False



class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
