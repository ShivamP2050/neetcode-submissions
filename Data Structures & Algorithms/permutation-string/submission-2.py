class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, 0
        perm = {}
        curr = {}

        for ch in s1:
            perm[ch] = perm.get(ch, 0) + 1

        while r < len(s2):
            if r - l >= len(s1):
                curr[s2[l]] -= 1
                if curr[s2[l]] == 0:
                    curr.pop(s2[l])
                l += 1

            curr[s2[r]] = curr.get(s2[r], 0) + 1
            
            if curr == perm:
                return True
            r += 1

        return False
