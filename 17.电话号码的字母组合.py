#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import List
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    #     if len(digits) == 0:
    #         return self.result
    #     self.getCombinations(digits, 0, "")
    #     return self.result
    
    # def __init__(self):
    #     self.letterMap = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    #     self.result = []

    # def getCombinations(self, digits, index, s):
    #     if index == len(digits):
    #         self.result.append(s)
    #         return
    #     digit = int(digits[index])
    #     letters = self.letterMap[digit]
    #     for letter in letters:
    #         self.getCombinations(digits, index + 1, s + letter)
    
        MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n  
        def dfs(i: int):
            if i == n:
                ans.append(''.join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i] = c  
                dfs(i + 1)
        dfs(0)
        return ans
# @lc code=end

