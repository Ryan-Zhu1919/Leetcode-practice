#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # i = 0
        # stack = []
        # while i < len(s):
        #     if s[i] in ['(', '[', '{']:
        #         stack.append(s[i])
        #     else:
        #         if not stack:
        #             return False
        #         if s[i] == ')' and stack[-1] != '(':
        #             return False
        #         if s[i] == ']' and stack[-1] != '[':
        #             return False
        #         if s[i] == '}' and stack[-1] != '{':
        #             return False
        #         stack.pop()
        #     i += 1
        # return not stack
        i = 0
        stack, left = [], ['(', '[', '{']
        while i < len(s):
            if s[i] in left:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] == ')' and stack[-1] != '(':
                    return False
                if s[i] == ']' and stack[-1] != '[':
                    return False
                if s[i] == '}' and stack[-1] != '{':
                    return False
                stack.pop() 
            i += 1
        return not stack        

# @lc code=end

