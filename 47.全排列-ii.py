#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        self.backtracking(nums, [], [False] * len(nums), res)
        return res

    def backtracking(self, nums, path, used, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, res)
            path.pop()
            used[i] = False
# @lc code=end

