class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        target = len(nums) // 3
        res = []
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > target and num not in res:
                res.append(num)
        return res

        
        