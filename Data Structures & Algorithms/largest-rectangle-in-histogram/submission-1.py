class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        height = []
        maxArea = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] >= heights[i]:
                tempIdx, tempH = stack.pop()
                width = i - tempIdx
                maxArea = max(maxArea, tempH * width)
                start = tempIdx

            stack.append((start, heights[i]))

        while stack:
            tempIdx, tempH = stack.pop()
            width = len(heights) - tempIdx
            maxArea = max(maxArea, tempH * width)

        return maxArea



            

        