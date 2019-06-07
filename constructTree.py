# pre-order: root - left - right
# in-order: left - root - right
# post-order: left - right - root

class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# construct a binary tree with pre-order and in-order
class Solution1:
    def reconstruct(self, pre, ino):
        if len(pre) == 0 or len(pre) != len(ino):
            return None
        elif len(pre) == 1:
            root = Tree(pre[0])
            return root
        else:
            root = Tree(pre[0])
            pos = ino.index(pre[0])
            root.left = self.reconstruct(pre[1:pos + 1], ino[:pos])
            root.right = self.reconstruct(pre[pos + 1:], ino[pos + 1:])
        return root


# test
def postorder(node):
    if node == None: return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=" ")


s = Solution1()
# pre = [1, 2, 4, 5, 3]
# ino = [4, 2, 5, 1, 3]
pre = [1, 2, 4, 7, 3, 5, 6, 8]
ino = [4, 7, 2, 1, 5, 3, 8, 6]


# root = s.reconstruct(pre, ino)
# postorder(root)


# construct a binary tree with inorder and post order
class Solution2:
    def reconstruct(self, ino, post):
        if len(post) == 0 or len(post) != len(ino):
            return None
        elif len(post) == 1:
            root = Tree(post[-1])
            return root
        else:
            root = Tree(post[-1])
            pos = ino.index(post[-1])
            num_right = len(post) - pos - 1
            num_left = pos
            root.left = self.reconstruct(ino[:pos], post[:pos])
            root.right = self.reconstruct(ino[pos + 1:], post[pos:-1])
        return root


# test
def preOrder(node):
    if node == None: return
    print(node.val, end=" ")
    preOrder(node.left)
    preOrder(node.right)


s2 = Solution2()
ino = [4, 7, 2, 1, 5, 3, 8, 6]
post = [7, 4, 2, 5, 8, 6, 3, 1]
root2 = s2.reconstruct(ino, post)
preOrder(root2)
