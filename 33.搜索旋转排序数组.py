#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            x = nums[mid]
            if target > nums[-1] >= x:
                right = mid - 1
            elif target <= nums[-1] < x:
                left = mid + 1
            elif x < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        else:
            return -1
# @lc code=end

