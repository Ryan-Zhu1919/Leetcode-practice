#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtracking(n, 0, 0, [], res)
        return res

    def backtracking(self, n, left, right, path, res):
        if left > n or right > n:
            return
        if left == n and right == n:
            res.append("".join(path))
            return
        if left < n:
            path.append("(")
            self.backtracking(n, left + 1, right, path, res)
            path.pop()
        if right < left:
            path.append(")")
            self.backtracking(n, left, right + 1, path, res)
            path.pop()
# @lc code=end

