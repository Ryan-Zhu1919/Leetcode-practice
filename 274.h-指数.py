#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#
from typing import List
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            cnt[min(c, n)] += 1  
        s = 0
        for i in range(n, -1, -1):  
            s += cnt[i]
            if s >= i: 
                return i
# @lc code=end

