class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        res = 0
        curr = 0

        
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            for i in count:
                if count[i] > curr:
                    curr = count[i]
                
            while (r - l + 1) - curr > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

 
        return res

        