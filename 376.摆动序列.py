#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        prediff, curdiff = 0, 0
        res = 1
        for i in range(len(nums) - 1):
            curdiff = nums[i + 1] - nums[i]
            if (curdiff < 0 and prediff >= 0) or (curdiff > 0 and prediff <=0):
                res += 1
                prediff = curdiff
        return res
# @lc code=end

