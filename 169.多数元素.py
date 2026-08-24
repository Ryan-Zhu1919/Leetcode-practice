#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter()
        n = len(nums)
        for c in nums:
            cnt[c] += 1
            if cnt[c] > n // 2:
                return c
# @lc code=end

