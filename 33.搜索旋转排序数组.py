#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     x = nums[mid]
        #     if target > nums[-1] >= x:
        #         right = mid - 1
        #     elif target <= nums[-1] < x:
        #         left = mid + 1
        #     elif x < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # if nums[left] == target:
        #     return left
        # else:
        #     return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1                       
# @lc code=end

