#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        self.backtracking(nums, 0, [], res)
        return res

    def backtracking(self, nums, startindex, path, res):
        if startindex > len(nums):
            return
        res.append(path[:])
        for i in range(startindex, len(nums)):
            if i > startindex and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, res)
            path.pop()
# @lc code=end

