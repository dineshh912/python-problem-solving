"""
Given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contain a single digit.
add the two numbers and return the sum as linked list.

l1 = [2,4,3], l2 = [5,6,4]
o = [7,0,8]

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def addTwoNumbers(l1: ListNode, l2: ListNode):
    
    carry = 0
    while l1 or l2:
        value_1 = l1.val if l1 else 0
        value_2 = l2.val if l2 else 0

        val = value_1 + value_2 + carry

        carry = val // 10
        val = val % 10

        



addTwoNumbers([2,4,3], [5,6,4])