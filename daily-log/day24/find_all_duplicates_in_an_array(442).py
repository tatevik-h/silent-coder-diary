class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        distinct_items = set()
        res = []
        for elem in nums:
            if elem in distinct_items:
                res.append(elem)
            else:
                distinct_items.add(elem)

        return res
      
