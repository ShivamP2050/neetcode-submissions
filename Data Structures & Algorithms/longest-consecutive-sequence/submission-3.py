class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numeros = set(nums)

        for i in numeros:
            if i - 1 not in numeros:
                temp = 1
                while i + 1 in numeros:
                    temp += 1
                    i += 1
                res = max(temp, res)


        return res
        