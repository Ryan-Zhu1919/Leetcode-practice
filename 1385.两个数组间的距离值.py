#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#
from typing import List
# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        ans = 0
        j = 0
        for i in range(len(arr1)):
            while j < len(arr2) and arr2[j] < arr1[i] - d:
                j += 1
            if j == len(arr2) or arr2[j] > arr1[i] + d:
                ans += 1
        return ans
# @lc code=end

