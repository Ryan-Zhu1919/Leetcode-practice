#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        self.backtracking(n, k, 1, [], res)
        return res
    def backtracking(self, n, k, startindex, path, res):
            if len(path) == k:
                res.append(path[:])
                return
            # for i in range(startindex, n + 1):
            for i in range(startindex, n - (k - len(path)) + 2):#剪枝优化
                path.append(i)
                self.backtracking(n, k, i + 1, path, res)
                path.pop()
# @lc code=end

