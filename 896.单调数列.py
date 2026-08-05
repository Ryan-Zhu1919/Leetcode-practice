#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] < nums[-1]:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
        else:
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
        return True
# @lc code=end

