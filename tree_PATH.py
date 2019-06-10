class Tree():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePathSUm(self, root):
        res = []

        def dfs(root, path):
            if root:
                path += str(root.val)
                if root.left == None and root.right == None:
                    res.append(path)
                if root.left != None:
                    path += '->'
                    dfs(root.left, path)
                if root.right != None:
                    path += '_>'
                    dfs(root.right, path)

        dfs(root, '')
        return res

    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        result = []
        tmp = [root]
        while len(tmp):
            cur = tmp.pop(0)
            result.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
        return result

    def isBalanced(self, root):
        self.flag = True
        self.treeDepth(root)
        return self.flag

    def treeDepth(self, root):
        if not root:
            return 0
        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)
        if abs(left - right) > 1:
            self.flag = False
        return self.flag


if __name__ == '__main__':
    s = Solution()
    tree = Tree(1)
    tree.left = Tree(2)
    tree.left.right = Tree(5)
    tree.right = Tree(3)
    print(s.binaryTreePathSUm(tree))
    print(s.PrintFromTopToBottom(tree))
    print(s.isBalanced(tree))
