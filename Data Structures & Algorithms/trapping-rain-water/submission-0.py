class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = [0] * len(height)
        mins = 0
        currMax = 0
        for i, num in enumerate(height):
            maxLeft.append(currMax)
            currMax = max(currMax, num)
        print(maxLeft)
        currMax = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = (currMax)
            currMax = max(currMax, height[i])
        for i in range(len(height)):
            total = min(maxRight[i], maxLeft[i]) - height[i]
            if total > 0:
                mins += total
        return mins            

        