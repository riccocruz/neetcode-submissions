# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def traverse(n):
            if n.val > val:
                if not n.left:
                    n.left = TreeNode(val)
                    return
                traverse(n.left)
            else:
                if not n.right:
                    n.right = TreeNode(val)
                    return
                traverse(n.right)
        traverse(root)
        return root