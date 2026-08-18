#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#
from typing import List
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        ans = -1
        left, s = 0, 0
        if target < 0:
            return -1
        for right, c in enumerate(nums):
            s += c
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        if ans < 0:
            return -1
        else:
            return len(nums) - ans
# @lc code=end

