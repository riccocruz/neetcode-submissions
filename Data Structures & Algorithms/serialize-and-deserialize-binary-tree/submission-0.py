# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = ""
        
        level = [root]
        while level:
            res += ",".join(str(n.val if n else 'None') for n in level)
                
            children = []
            for n in level:
                if n:
                    children.append(n.left)
                    children.append(n.right)
            if any(child for child in children):
                level = children
                res += "--"
            else:
                break

        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        rows = data.split('--')
            
        root = TreeNode(int(rows[0][0]))
        level = [root]
        for row in rows[1:]:
            cur = row.split(',')
            temp = []
            parent_index = 0
            i = 0
            while i < len(cur):
                if cur[i] != 'None':
                    node = TreeNode(int(cur[i]))
                    level[parent_index].left = node
                    temp.append(node)
                i += 1
                if cur[i] != 'None':
                    node = TreeNode(int(cur[i]))
                    level[parent_index].right = node
                    temp.append(node)
                i += 1
                parent_index += 1
            if not temp:
                break
            level = temp

        return root

