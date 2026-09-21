#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
from typing import List
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s, 0, [], res)
        return res

    def backtracking(self, s, startindex, path, res):
        if startindex == len(s):
            res.append(path[:])
            return res
        for i in range(startindex, len(s)):
            if self.isPalindrome(s, startindex, i):
                path.append(s[startindex:i + 1])
                self.backtracking(s, i + 1, path, res)
                path.pop()

    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
# @lc code=end

