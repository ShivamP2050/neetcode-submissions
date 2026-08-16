# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, high):
            if node is None:
                return
            
            l, r = node.left, node.right

            if node.val >= high:
                nonlocal count
                count += 1
                
                if l:
                    dfs(l, node.val)
                if r:
                    dfs(r, node.val)
            else:
                dfs(l, high)
                dfs(r, high)

        if root:
            dfs(root, root.val)
        else:
            return 0

        return count
        