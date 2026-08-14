class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * n
        if n == 0:
            return 0
        elif n < 2:
            return 1
        elif n < 3:
            return 2
        else:
            arr[n - 1], arr[n - 2] = 1, 1

        for i in range(n - 3, -1, -1):
            arr[i] = arr[i + 1] + arr[i + 2]

        return arr[0] + arr[1]



