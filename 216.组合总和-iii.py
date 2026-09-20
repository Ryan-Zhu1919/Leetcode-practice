#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtracking(n, k, 0, 1, [], res)
        return res

    def backtracking(self, n, k, sum, startindex, path, res):
        if sum > n:
            return
        if len(path) == k:
            if sum == n:
                res.append(path[:])
            return
        for i in range(startindex, 9 - (k - len(path)) + 2):
            path.append(i)
            sum += i
            self.backtracking(n, k, sum, i + 1, path, res)
            sum -= i
            path.pop()
# @lc code=end

