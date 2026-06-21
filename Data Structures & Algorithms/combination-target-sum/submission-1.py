class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        combo = []

        def dfs(i):
            if sum(combo) == target:
                res.append(combo.copy())
                return
            if sum(combo ) > target:
                return
            for num in range(i, len(nums)):
                if sum(combo) + nums[num] > target:
                    return
                combo.append(nums[num])
                dfs(num)
                combo.pop()
                

        dfs(0)
        return res