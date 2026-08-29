#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
from typing import List
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = set(nums1)
        ans = []
        for num in nums2:
            if num in temp:
                temp.remove(num)
                ans.append(num)
        return ans
# @lc code=end

