class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        currMin = float("inf")

        while l <= r:
            mid = (l + r) // 2
            currMin = min(nums[mid], currMin)
            if nums[l] <= nums[mid]:
                if nums[r] < nums[l]:
                    l = mid +1
                else:
                    r = mid - 1
            else:
                r = mid - 1

        return currMin

        
        