#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
from typing import List
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        stack = []
        i = 0
        while i < len(nums)-1:
            stack.append(nums[i])
            if nums[i+1] == nums[i]:
                stack.pop()
                i += 2
            else:
                i += 1
        if stack:
            return stack[0]
        else:
            return nums[len(nums)-1]
# @lc code=end

