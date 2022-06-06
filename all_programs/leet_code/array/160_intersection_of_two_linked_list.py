"""
    Given the heads of two singly linked list headA and headB, return the node
    at which the two lists intersect. if two linked list have no intersection return null.

    intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1

    intersect at 2
    
"""

from pyrsistent import b


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode):
    visited = set()

    while headA:
        visited.add(headA)
        headA = headA.next

    while headB:
        if headB in visited:
            return headB
        headB = headB.next
    
    return None
            

def getIntersection(headA, headB):
    len_a, len_b = 0, 0

    # FInd the length
    while headA:
        a += 1
        headA = headA.next
    
    while headB:
        b += 1
        headB = headB.next

    # find which node is longest in length and its differnece
    if a > b:
        longest = headA
        diff = a - b
        shortest = headB
    else:
        longest = headB
        diff = b - 1
        shortest = headA
    
    i = 0
    while i < diff:
        i += 1
        longest = longest.next
    
    while longest != shortest:
        longest = longest.next
        shortest = shortest.next
    
    return longest
            


print(getIntersectionNode([4,1,8,4,5], [5,6,1,8,4,5]))