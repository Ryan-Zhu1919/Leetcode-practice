#
# @lc app=leetcode.cn id=3795 lang=python3
#
# [3795] 不同元素和至少为 K 的最短子数组长度
#
from math import inf
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        ans = inf
        total, left = 0, 0
        cnt = Counter()
        for right, c in enumerate(nums):
            cnt[c] += 1
            if cnt[c] == 1:
                total += c
            while total >= k:
                ans = min(ans, right - left + 1)
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    total -= nums[left]
                left += 1
        if ans == inf:
            return -1
        else:
            return ans
# @lc code=end

