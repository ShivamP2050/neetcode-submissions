# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                return False
        elif (not p and not q):
            return True
        else:
            return False


        arr1 = []
        arr2 = []
        stck1 = []
        stck2 = []
        stck1.append(p)
        stck2.append(q)

        while stck1 and stck2:
            tree1 = stck1.pop(0)
            tree2 = stck2.pop(0)

            arr1.append(tree1)
            arr2.append(tree2)
            
            if not tree1 and not tree2:
                continue
            elif not tree1 or not tree2:
                return False

            
            if ((tree1.val == tree2.val)):
                stck1.append(tree1.left)
                stck1.append(tree1.right)
                stck2.append(tree2.left)
                stck2.append(tree2.right)
            else:
                return False
                
        return True




