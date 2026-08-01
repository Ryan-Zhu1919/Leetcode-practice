#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#

# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
       n = 0
       for i in range(len(arr)):
           for j in range(i + 1,len(arr)):
               for k in range(j + 1,len(arr)):
                   if abs(arr[i]-arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                     n += 1
       return n
# @lc code=end

