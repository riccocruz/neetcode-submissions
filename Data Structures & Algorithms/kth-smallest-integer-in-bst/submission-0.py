# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = 0
        res = None
        def traverse(n):
            nonlocal inorder
            nonlocal res
            if not n:
                return
            traverse(n.left)
            inorder += 1
            if inorder == k:
                res = n
                return
            traverse(n.right)

        traverse(root)
        return res.val