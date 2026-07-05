# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = -1

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) >= 2:
                self.res = -2

            return 1 + max(left, right)

        dfs(root)
        if self.res == -1:
            return True
        else:
            return False

        

        
        