#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, [], res)
        return res

    def backtracking(self, candidates, target, sum, startindex, path, res):
        if sum > target:
            return
        if sum == target:
            res.append(path[:])
            return
        for i in range(startindex, len(candidates)):
            if i > startindex and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            sum += candidates[i]
            self.backtracking(candidates, target, sum, i + 1, path, res)
            path.pop()
            sum -= candidates[i]
# @lc code=end

