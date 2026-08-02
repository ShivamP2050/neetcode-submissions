class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        temp = []

        # i = 0 -> 1 -> 2
        # temp = [1, 2, 3] -> 
        #res = [[1], [1, 2], [1, 2, 3], ] 

        def dfs(i):
            if i >= len(nums):
                return
            temp.append(nums[i])
            res.append(temp.copy())
            dfs(i + 1)

            temp.pop()
            dfs(i + 1)

        dfs(0)
        return res

