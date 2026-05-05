# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def traverse(n: TreeNode, maxval: int):
            nonlocal res
            if not n:
                return None
            
            if n.val >= maxval:
                res += 1
                maxval = n.val
            
            traverse(n.left, maxval)
            traverse(n.right, maxval)

        
        traverse(root, -float('inf'))
        return res