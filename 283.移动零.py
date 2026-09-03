#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针
        # left, right = 0, 0
        # while right < len(nums):
        #     if nums[right] != 0:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #     right += 1

        # 栈
        size = 0
        for num in nums:
            if num:
                nums[size] = num
                size += 1
        for i in range(size, len(nums)):
            nums[i] = 0
                # @lc code=end

