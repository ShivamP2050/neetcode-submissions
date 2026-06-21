class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        


        def validAns(close, ope):
            if close == ope == n:
                res.append("".join(stack))
                return

            if ope < n:
                stack.append("(")
                validAns(close, ope + 1)
                stack.pop()

            if ope > close:
                stack.append(")")
                validAns(close + 1, ope)
                stack.pop()
         

        validAns(0, 0)
        return res

            

        