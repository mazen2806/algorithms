#https://leetcode.com/problems/same-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)


if __name__ == "__main__":
    s = Solution()
    p_tree = TreeNode(1, TreeNode(2), TreeNode(3))
    q_tree = TreeNode(1, TreeNode(2), TreeNode(3))
    print(s.is_same_tree(p_tree, q_tree))