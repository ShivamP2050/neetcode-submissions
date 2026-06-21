class Solution:
    def minWindow(self, s: str, t: str) -> str:
        bank = {}
        st = set()
        for i in t:
            bank[i] = bank.get(i, 0) + 1
            st.add(i)

        res = ""
        store = {}
        need = len(bank)
        have = 0
        l = 0
        for r in range(len(s)):
            store[s[r]] = store.get(s[r], 0) + 1
            if s[r] in st and store[s[r]] == bank[s[r]]:
                have += 1
            if have == need and (len(res) > r - l or res == ""):
                res = s[l:r+1]
            while have == need:
                store[s[l]] -= 1
                if store[s[l]] < bank.get(s[l], 0):
                    have -= 1
                if len(res) > r - l:
                    res = s[l:r+1]
                l += 1
                
        return res



