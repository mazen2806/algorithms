# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.
# Example:
# Given binary tree:
#
#     A
#    / \
#   B   C
#     /  \
#    D    E
# return its depth = 3.


class TreeNode:
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def max_depth(self, node):
        if node:
            left_depth = self.max_depth(node.left)
            right_depth = self.max_depth(node.right)

            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1
        else:
            return 0


root = TreeNode("A", TreeNode("B", None, None), TreeNode("C", TreeNode("D", None, None),  TreeNode("E", None, None)))
tree = Tree(root)
print(tree.max_depth(root))
