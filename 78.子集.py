#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, 0, [], res)
        return res

    def backtracking(self, nums, startindex, path, res):
        if startindex > len(nums):
            return
        res.append(path[:])
        for i in range(startindex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, res)
            path.pop()
# @lc code=end

