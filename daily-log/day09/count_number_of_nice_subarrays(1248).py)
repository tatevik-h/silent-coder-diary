class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = {0:1}
        counter = 0
        for num in nums:
            if num %2 == 1:
                prefix_sum +=1
            if prefix_sum - k in prefix_map:
                counter += prefix_map[prefix_sum - k]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        
        return counter
