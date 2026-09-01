class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []
        mp = {"2":["a", "b", "c"], 
        "3":["d", "e", "f"], 
        "4":["g", "h", "i"], 
        "5":["j", "k", "l"], 
        "6":["m", "n", "o"], 
        "7":["p", "q", "r", "s"], 
        "8":["t", "u", "v"], 
        "9":["w", "x", "y", "z"]}

        res = []
        temp = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(temp))
                return

            comp = mp[digits[i]]
            for ch in comp:
                temp.append(ch)
                dfs(i + 1)
                temp.pop()
            
            
        dfs(0)
        return res


        