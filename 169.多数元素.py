#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
# from collections import Counter
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 暴力
        # cnt = Counter()
        # n = len(nums)
        # for c in nums:
        #     cnt[c] += 1
        #     if cnt[c] > n // 2:
        #         return c
        
        # 摩尔投票法
        ans, votes = 0, 0
        for num in nums:
            if votes == 0:
                ans = num
            if num == ans:
                votes += 1
            else:
                votes -= 1
        return ans
# @lc code=end

