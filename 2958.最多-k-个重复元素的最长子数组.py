#
# @lc app=leetcode.cn id=2958 lang=python3
#
# [2958] 最多 K 个重复元素的最长子数组
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, c in enumerate(nums):
            cnt[c] += 1
            while cnt[c] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right -left + 1)
        return ans
# @lc code=end

