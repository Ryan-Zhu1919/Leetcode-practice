#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
from typing import List
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        n, k = len(nums), k % len(nums)
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)    
# @lc code=end

