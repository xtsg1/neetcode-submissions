# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# first attempt nov 12

# QUE
# both linked lists
# both sorted? free sort operation already....
# basically like a zipper merge
# but list 1 takes precedence
# merged list must be sorted! 

# APPROACH
# each list gets a head pointer
# each list1 node should point at the corresponding list2 node 1 -> 1, 2 -> 2, etc
# each list2 node should point at the next list1 node: 1 -> 2, 2 -> 3 etc
# one pointer for each list i,j
# requires 2 temp continuation var x,y to store the next node for list1
# stopping condition: second j pointer points to null
# need to keep track of head once linkedlist is modified in place

# WALKTHROUGH

# 1 > 2 > 4
# 1 > 3 > 5

# i 1
# j 1
# x 2
# y 3
# i 1
# j 2
# i 2
# j 3

# 1 > 1 > 2 > 3



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        i = list1
        j = list2

        head = dummy = tail = ListNode()

        while i and j:

            if i.val <= j.val:
                tail.next = i
                i = i.next
            elif j.val < i.val:
                tail.next = j
                j = j.next
            
            tail = tail.next

        tail.next = i or j
            
        return head.next
            
                
                


            






        