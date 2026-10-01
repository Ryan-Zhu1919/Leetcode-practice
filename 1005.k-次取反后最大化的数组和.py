#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#
from typing import List
# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums1 = sorted(nums)
        for i in range(len(nums)):
            if k > 0 and nums1[i] < 0:
                nums1[i] = -nums1[i]
                k -= 1
        nums2 = sorted(nums1)
        if k > 0 and k % 2 == 1:
            nums2[0] = -nums2[0]
        return sum(nums2)
# @lc code=end

