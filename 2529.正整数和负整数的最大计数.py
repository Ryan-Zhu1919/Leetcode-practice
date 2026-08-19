#
# @lc app=leetcode.cn id=2529 lang=python3
#
# [2529] 正整数和负整数的最大计数
#
from typing import List
# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def lower_bound(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left  
        count1 = lower_bound(nums, 0)     
        start = lower_bound(nums, 1)      
        count2 = len(nums) - start     
        return max(count1, count2)
# @lc code=end

