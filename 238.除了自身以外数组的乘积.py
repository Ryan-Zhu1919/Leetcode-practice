#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除了自身以外数组的乘积
#
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        return [left[i] * right[i] for i in range(n)]
# @lc code=end

