# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # check the path of left and right subtree
        # cursum = max(n.val, n.val + left, n.val + right)
        # maxsum = max(maxsum, left + right + n.val, cursum)
        res = float('-inf')

        def traverse(n):
            if not n:
                return 0
            
            nonlocal res
            left = traverse(n.left)
            right = traverse(n.right)

            cursum = max(n.val, n.val + left, n.val + right)
            res = max(res, left + right + n.val, cursum)
            return cursum
        
        traverse(root)
        return res
            