#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # def get_num(node):
        #     vals = []
        #     while node:
        #         vals.append(str(node.val))
        #         node = node.next
        #     return int(''.join(vals[::-1]))
        # s1 = get_num(l1)
        # s2 = get_num(l2)
        # s = s1 + s2
        # head = ListNode(0)
        # cur = head
        # res = str(s)
        # for c in res[::-1]:
        #     cur.next = ListNode(int(c))
        #     cur = cur.next
        # return head.next
        def dfs(a, b, carry):
            if a is None and b is None and carry == 0:
                return None
            total = carry
            if a:
                total += a.val
            if b:
                total += b.val
            digit = total % 10
            next_carry = total // 10
            node = ListNode(digit)
            node.next = dfs(a.next if a else None, b.next if b else None, next_carry)
            return node
        return dfs(l1, l2, 0)
# @lc code=end

