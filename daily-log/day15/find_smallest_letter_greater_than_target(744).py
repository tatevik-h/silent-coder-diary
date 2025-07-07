class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = left + ((right -  left)//2)

            if target >= letters[mid]:
                left = mid + 1
            else:
                right = mid -1

        if left < len(letters):
            return letters[left ]

        return letters[0]
        
