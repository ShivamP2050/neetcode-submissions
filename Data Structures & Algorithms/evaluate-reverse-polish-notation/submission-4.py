class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        total = 0
        for i in tokens:
            if i == "+":
                total = nums.pop() + nums.pop()
                nums.append(total)
            elif i == "*":
                total = int(nums.pop()) * int(nums.pop())
                nums.append(total)
            elif i == "-":
                a, b = nums.pop(), nums.pop()
                nums.append(b - a)
            elif i == "/":
                a, b = nums.pop(), nums.pop()
                nums.append(int(float(b)/a))
            else:
                nums.append(int(i))
            print(nums)
        return nums[0]
        