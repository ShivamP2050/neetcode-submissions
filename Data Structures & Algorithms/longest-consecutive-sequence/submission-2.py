class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numeros = set(nums)

        for i in numeros:
            temp = 1
            if i - 1 not in numeros:
                
                while i + 1 in numeros:
                    temp += 1
                    i += 1
            res = max(temp, res)


        return res
        