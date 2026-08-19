#
# @lc app=leetcode.cn id=2300 lang=python3
#
# [2300] 咒语和药水的成功对数
#
from typing import List
# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def lower_bound(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:  
                    right = mid - 1
                else:
                    left = mid + 1
            return left  

        potions.sort()          
        pairs = []
        for spell in spells:
            needed = (success + spell - 1) // spell
            index = lower_bound(potions, needed)
            pairs.append(len(potions) - index)
        return pairs
# @lc code=end

