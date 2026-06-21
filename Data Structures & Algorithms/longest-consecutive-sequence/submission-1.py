class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        for i in nums:
            temp = 1
            while i - 1 in nums:
                temp += 1
                i -= 1
            res = max(res, temp)

        return res
        