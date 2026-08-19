class Solution:
    def rob(self, nums: List[int]) -> int:

        money = [0] * len(nums)

        if len(nums) == 1:
            return nums[0]
        elif len(nums) > 2:
            money[-1] = nums[-1]
            money[-2] = nums[-2]
        else:
            return max(nums[-1], nums[-2])

        currMax = max(money[-1], money[-2])
        establishedMax = money[-1]

        for i in range(len(nums) - 3, -1, -1):
            money[i] = establishedMax + nums[i]
            currMax = max(currMax, money[i])
            establishedMax = max(establishedMax, money[i + 1])

        return currMax




        