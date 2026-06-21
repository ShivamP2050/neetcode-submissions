class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        l = 0
        r = 0

        while l < len(temperatures):
            if temperatures[r] > temperatures[l]:
                res[l] = r - l
                l += 1
                r = l
            elif r == len(temperatures) - 1:
                l += 1
                r = l
            else:
                r += 1
        return res
        