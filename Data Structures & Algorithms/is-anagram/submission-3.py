class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sTable = defaultdict(int)
        tTable = defaultdict(int)
        for i in s:
            sTable[i] += 1
        for i in t:
            tTable[i] += 1
        return tTable == sTable


