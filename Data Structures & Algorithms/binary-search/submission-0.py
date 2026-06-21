class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        r, l = 0, len(nums)
        while r < l and nums:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                l, mid = mid, ((l - r) // 2) + r
            else:
                r, mid = mid + 1, ((l - r) // 2) + r
        return -1