#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 非递减子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.backtracking(nums, 0, [], res)
        return res

    def backtracking(self, nums, startindex, path, res):
        if len(path) >= 2:
            res.append(path[:])
        if startindex > len(nums):
            return
        used = set()
        for i in range(startindex,len(nums)):
            if (len(path) > 0 and nums[i] < path[-1]) or nums[i] in used:
                continue
            used.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, res)
            path.pop()
# @lc code=end

