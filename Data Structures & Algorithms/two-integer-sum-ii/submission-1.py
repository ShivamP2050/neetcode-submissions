class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = 0, 0

        while l < len(numbers):
            total = numbers[l] + numbers[r]
            if total < target:
                r += 1
            elif total == target:
                return [l + 1, r + 1]
            else:
                l += 1
                r  = l
            if r >= len(numbers):
                l += 1
                r  = l
        return []


        