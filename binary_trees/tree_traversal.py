""" Binary Tree Traversal functions """
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print('Inorder: {}'.format(root.data))
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print('Preorder: {}'.format(root.data))
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print('Postorder: {}'.format(root.data))