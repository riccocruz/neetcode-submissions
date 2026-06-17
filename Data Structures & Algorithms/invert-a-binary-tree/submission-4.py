# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # simple recursive
        # if not root:
        #     return
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # # loop
        # if not root:
        #     return
        # stack = [root]
        # while stack:
        #     n = stack.pop()
        #     n.left, n.right = n.right, n.left
        #     if n.right:
        #         stack.append(n.right)
        #     if n.left:
        #         stack.append(n.left)
        # return root

        # # bfs
        if not root:
            return
        dq = deque([root])
        while dq:
            n = dq.popleft()
            n.left, n.right = n.right, n.left
            if n.left:
                dq.append(n.left)
            if n.right:
                dq.append(n.right)
        return root
