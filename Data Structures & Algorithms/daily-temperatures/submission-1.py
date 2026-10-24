class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                t, indx = stack.pop()
                result[indx] = i - indx

            stack.append((temp, i))

        return result
        