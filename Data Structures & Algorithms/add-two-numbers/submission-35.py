# GREEN 2026-11-17 | cold, alone, no hints; fixed own bugs by tracing | O(max(m,n)) time and space (output list) | cleanup: int carry (s // 10, s % 10) instead of bool flag; "if l1: s += l1.val; l1 = l1.next" instead of 4 ternaries | next review ~Nov 24
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# attempt nov 17

# QUESTION
# reverse order so 321 is stored 1 2 3
# ones tens hundreds etc
# one digit per node thankfully
# sum of two numbers return a linked list

# APPROACH
# ok so 1 10 100s columns makes this easier
# can simply add
# create a new linked list to track outputs instead of playing switcheroo with the existing lists
# extra space but whatever lets make it work first
# consider cases where l1 and l2 are different lengths
# sums over 10 must be carried like regular addition
# while loop for summing when either l1 or l2 have digits still OR carry? 

# time/space both O(n)

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        h = ListNode()
        t = h

        carry = False 
        while l1 or l2 or carry:

            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            s = n1 + n2

            if carry:
                s += 1
                carry = False #dealt with...turn flag back off
            if s >= 10:
                carry = True
                s -= 10

            t.next = ListNode(val=s, next=None)

            t = t.next     #ff all lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        
        h = h.next
        return h
        






        