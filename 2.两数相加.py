#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_num(node):
            vals = []
            while node:
                vals.append(str(node.val))
                node = node.next
            return int(''.join(vals[::-1]))
        s1 = get_num(l1)
        s2 = get_num(l2)
        s = s1 + s2
        head = ListNode(0)
        cur = head
        for c in str(s)[::-1]:
            cur.next = ListNode(int(c))
            cur = cur.next
        return head.next
# @lc code=end

