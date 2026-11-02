# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            view = queue.popleft()
            length = len(queue)
            if view:
                res.append(view.val)

                if view.right:
                    queue.append(view.right)
                if view.left:
                    queue.append(view.left)

            for i in range(length):
                temp = queue.popleft()

                if temp.right:
                    queue.append(temp.right)
                if temp.left:
                    queue.append(temp.left)

        return res

        
        