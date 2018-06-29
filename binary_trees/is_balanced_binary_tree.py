'''
Problem 9.1: Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced
'''

def is_balanced_binary_tree(tree):
    if not tree:
        return True
    
    height_diff = get_height(tree.left) - get_height(tree.right)

    if abs(height_diff) > 1:
        return False
    else:
        return is_balanced_binary_tree(tree.left) and is_balanced_binary_tree(tree.right)


def get_height(tree):
    # Base case
    if not tree:
        return -1
    return max(get_height(tree.left), get_height(tree.right)) + 1