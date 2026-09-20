#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, [], res)
        return res
    def backtracking(self, candidates, target, sum, startindex, path, res):
        if sum == target:
            res.append(path[:])
            return
        for i in range(startindex, len(candidates)):
            if sum + candidates[i] > target:
                break
            sum += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, sum, i, path, res)
            sum -= candidates[i]
            path.pop()
# @lc code=end

