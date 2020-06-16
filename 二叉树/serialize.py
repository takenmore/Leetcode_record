from collections import deque
'''
    序列化和反序列化二叉树
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = []
        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.pop()
            if cur:
                s.append(str(cur.val))
                queue.appendleft(cur.left)
                queue.appendleft(cur.right)
            else:
                s.append("null")
            s.append(",")
        res = "".join(s)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split(",")
        if tree[0] == "null":
            return None
        queue = deque()
        root = TreeNode(int(tree[0]))
        queue.appendleft(root)
        i = 1
        while queue:
            cur = queue.pop()
            if cur == None:
                continue
            cur.left = TreeNode(int(tree[i])) if tree[i] != "null" else None
            cur.right = TreeNode(int(tree[i + 1])) if tree[i+1] != "null" else None
            i += 2
            queue.appendleft(cur.left)
            queue.appendleft(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
codec = Codec()
s = codec.serialize(root)

codec.deserialize(codec.serialize(root))
