class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        r = 0
        s1 = sorted(s1)
        while r < len(s2):
            tmp = sorted(s2[l: r + 1])
            if (tmp == s1):
                return True
            while r - l + 1 >= len(s1):
                l += 1

            r += 1

        return False
        