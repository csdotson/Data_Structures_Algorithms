'''
Problem 9.1: Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced. More 'pythonic' solution.
'''
import collections

def is_balanced_binary_tree_pythonic(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # Base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(balanced, height)

    return check_balanced(tree).balanced