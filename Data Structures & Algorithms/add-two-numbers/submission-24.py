# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# QUESTION
# nonempty
# each LIST represents a single NUMBER noneg int
# reverse order
# one digit per node
# no leading 0s

# APPROACH
# reverse order means beginning with 1s columns 
# this actually makes addition easier
# numbers may be different lengths
# start with pointer at 1s column -> 10s, ->20s
# implement a carrying method if >= 10
# add 1 in next sum
# move pointers
# at the end if either list is missing pointers


# walkthrough
# 1 2 3
# 4 5 6

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sums = ListNode()
        head = sums


        carry = False

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2
            if carry:
                s += 1
                carry = False

            if s >= 10:
                s -= 10
                carry = True

            sums.next = ListNode(val=s, next=None)
            sums = sums.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return head.next


            
        