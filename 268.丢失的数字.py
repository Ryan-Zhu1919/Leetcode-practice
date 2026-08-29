#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#
from typing import List
# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if num != i:
                return i
        return len(nums)
# @lc code=end

