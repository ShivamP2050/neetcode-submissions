class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        tracker = set()
        nums.sort()

        res = []
        temp = []

        def dfs(i):
            if i >= len(nums):
                res.append(temp.copy())
                return
            
            val = nums[i]
            tracker.add(val)
            temp.append(val)
            dfs(i+1)

            temp.pop()
            jump = i + 1
            while jump < len(nums) and nums[jump] == val:
                jump += 1
            dfs(jump)

            


        dfs(0)
        return res

            
        