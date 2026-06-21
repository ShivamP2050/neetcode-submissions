class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            tot = 1
            for j in range(len(nums)):
                if j != i:
                    tot *= nums[j]
            res.append(tot)
        return res
        