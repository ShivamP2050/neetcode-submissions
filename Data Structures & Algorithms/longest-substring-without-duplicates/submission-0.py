class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxC = 0
        chars = []

        while r < len(s):
            while s[r] in chars:
                chars.pop(0)
            chars.append(s[r])
            maxC = max(maxC, len(chars))
            r += 1
                
        return maxC
        

        