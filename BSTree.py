# construct binary search tree from inorder and postorder
# test the binary search tree with preorder
# time complexity: O(n^2)

# Tree traversal
# preorder : Root/Left/Right
# inorder: Left/Root/Right
# postorder: Left/Right/Root
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(arr, start, end, value):
    i = 0
    for i in range(start, end + 1):
        if (arr[i] == value):
            break
    return i


def buildUtil(In, post, inStr, inEnd, pIdx):
    if (inStr > inEnd):
        return None
    # pIdx is the last index of postorder
    node = Node(post[pIdx[0]])
    pIdx[0] -= 1

    if (inStr == inEnd):
        return node

    # find the idx of root in the Inorder traversal
    iIndex = search(In, inStr, inEnd, node.data)
    node.right = buildUtil(In, post, iIndex + 1, inEnd, pIdx)
    node.left = buildUtil(In, post, inStr, iIndex - 1, pIdx)
    return node


def buildTree(In, post):
    n = len(In)
    p1Index = [n - 1]
    p2Index = [0]
    if a == 1:
        return buildUtil(In, post, 0, n - 1, p1Index)


def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


def postOrder(node):
    if node == None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data, end=" ")


if __name__ == '__main__':
    In = [4, 8, 2, 5, 1, 6, 3, 7]
    Post = [8, 4, 5, 2, 6, 7, 3, 1]
    Pre = [1, 2, 4, 8, 5, 3, 6, 7]
    root = buildTree(In, Post)
    print("\npostorder of the constructed tree")
    postOrder(root)
