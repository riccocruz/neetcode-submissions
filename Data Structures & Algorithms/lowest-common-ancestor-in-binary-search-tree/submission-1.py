# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(n):
            if p.val <= n.val <= q.val or p.val >= n.val >= q.val:
                return n
            if p.val < n.val or q.val < n.val:
                return lca(n.left)
            else:
                return lca(n.right)
        return lca(root)