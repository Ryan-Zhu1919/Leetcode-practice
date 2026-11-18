#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import List
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for a in range(n - 3): 
            x = nums[a]
            if a and x == nums[a - 1]: 
                continue
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target: 
                break
            for b in range(a + 1, n - 2): 
                y = nums[b]
                if b > a + 1 and y == nums[b - 1]: 
                    continue
                if x + y + nums[b + 1] + nums[b + 2] > target: 
                    break
                c = b + 1
                d = n - 1
                while c < d:
                    s = x + y + nums[c] + nums[d] 
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else: 
                        ans.append([x, y, nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]: 
                            c += 1
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]: 
                            d -= 1
        return ans
# @lc code=end

