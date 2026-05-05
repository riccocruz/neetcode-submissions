# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        level = [root]
        while level:
            res.append(level[-1].val)

            children = []
            for n in level:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            level = children
        return res