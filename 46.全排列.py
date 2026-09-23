#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, [], res)
        return res

    def backtracking(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.backtracking(nums, path, res)
            path.pop()
# @lc code=end

