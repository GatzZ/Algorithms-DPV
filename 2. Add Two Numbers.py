# # 2. Add Two Numbers
# Difficulty: Medium
#
# >You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# >Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# >Output: 7 -> 0 -> 8
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        currNode = head
        carry = 0

        while l1 or l2 or carry:
            # if carry, then it already added a new node

            currNode.next = ListNode(carry)
            currNode = currNode.next

            if l1:
                currNode.val += l1.val
                l1 = l1.next

            if l2:
                currNode.val += l2.val
                l2 = l2.next

            carry = currNode.val / 10
            currNode.val = currNode.val % 10

        return head.next  # drop the head node


l1 = ListNode(2)
l2 = ListNode(3)
print Solution().addTwoNumbers(l1, l2).val
