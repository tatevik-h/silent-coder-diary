class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix_sum = [0]*101

        for b, d in logs:
            prefix_sum[b-1950] += 1
            prefix_sum[d-1950] -= 1

        max_pop = 0
        curr_pop = 0
        max_y = 1950
        for i in range(101):
            curr_pop += prefix_sum[i]
            if max_pop < curr_pop:
                max_pop = curr_pop
                max_y = 1950 + i
        return max_y
      
