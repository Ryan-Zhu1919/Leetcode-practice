#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归法
        # res = []
        # def dfs(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return res

        # 迭代法
        res = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                res.append(node.val)
        return res
# @lc code=end

