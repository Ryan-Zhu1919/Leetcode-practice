#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        ans = left + right
        if root.left:
            if root.left.left is None and root.left.right is None:
                ans += root.left.val
        return ans
# @lc code=end

