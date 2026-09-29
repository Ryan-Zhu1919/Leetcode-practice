#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, count = float('-inf'), 0
        for i in range(len(nums)):
            count += nums[i]
            if count > res:
                res = count
            if count < 0:
                count = 0
        return res
# @lc code=end

