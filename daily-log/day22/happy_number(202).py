class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
 
        def get_next(number: int) -> int:
            total = 0
            while number > 0:
                val = number % 10
                total += val  ** 2
                number = number // 10

            return total


        while n != 1 and  n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
