#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.head = None
        self.dfs(root)

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.right)
        self.dfs(root.left)
        root.left = None
        root.right = self.head
        self.head = root
# @lc code=end

