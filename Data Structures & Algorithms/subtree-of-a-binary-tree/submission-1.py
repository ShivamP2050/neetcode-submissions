# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame():
            tempq = deque()
            tempq.append(start)
            tempq.append(subRoot)
            while tempq:
                print("hi")
                curr1 = tempq.pop()
                curr2 = tempq.pop()
                if curr1 and curr2 and curr1.val == curr2.val:
                    tempq.append(curr1.left)
                    tempq.append(curr2.left)
                    tempq.append(curr1.right)
                    tempq.append(curr2.right)
                elif curr1 == curr2:
                    pass
                else:
                    return False
            return True


        queue = deque()
        queue.append(root)
        start = None

        while queue:
            curr = queue.pop()
            if curr:
                if curr.val == subRoot.val:
                    start = curr
                    if isSame():
                        return True
                queue.append(curr.left)
                queue.append(curr.right)

        

        return False