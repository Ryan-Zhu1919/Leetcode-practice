#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        cur, total, start = 0, 0, 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start if total >= 0 else -1
# @lc code=end

