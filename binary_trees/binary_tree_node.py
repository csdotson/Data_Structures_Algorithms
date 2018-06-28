class BinaryTreeNode:
    """ Class to create binary tree node object """
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    """ Binary tree object """
    def __init__(self, root):
        self.root = root


if __name__ == "__main__":
    root = BinaryTreeNode('A')
    leaf1 = BinaryTreeNode('B')
    leaf2 = BinaryTreeNode('C')
    leaf3 = BinaryTreeNode('D')
    leaf4 = BinaryTreeNode('E')

    root.left = leaf1
    root.right = leaf2
    leaf1.left = leaf3
    leaf1.right = leaf4