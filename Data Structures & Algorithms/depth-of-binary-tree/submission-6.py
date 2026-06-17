# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # recursive
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # # iterative dfs
        # if not root:
        #     return 0
        # stack = [(root, 1)]
        # deepest = 1
        # while stack:
        #     n, cur = stack.pop()
        #     deepest = max(deepest, cur)
        #     if n.left:
        #         stack.append((n.left, 1 + cur))
        #     if n.right:
        #         stack.append((n.right, 1 + cur))

        # return deepest

        # bfs
        if not root:
            return 0
        dq = deque([(root, 1)])
        while dq:
            n, cur = dq.popleft()
            if n.left:
                dq.append((n.left, cur + 1))
            if n.right:
                dq.append((n.right, cur + 1))
            if not dq:
                return cur
        
