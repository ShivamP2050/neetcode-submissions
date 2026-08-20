# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque()

        queue.append(root)

        while queue:
            node = queue.pop()
            if node:
                if node.val < p.val and node.val > q.val or node.val < q.val and node.val > p.val or node.val == p.val or node.val == q.val:
                    return node
                else:
                    queue.append(node.left)
                    queue.append(node.right)
        return
            
        
            
        