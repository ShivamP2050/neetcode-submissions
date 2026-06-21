class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = []
        total = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            res.append(s[r])
            diff = max(count.values())
            while len(res) - diff > k:
                count[res.pop(0)] -= 1
                diff = max(count.values())
            total = max(total, len(res))
        return total


        