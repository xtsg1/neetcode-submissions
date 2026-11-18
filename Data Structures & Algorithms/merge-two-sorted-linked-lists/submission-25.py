# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# nov 18 rep

# QUESTION
# given two lists
# they are already ordered
# must merge the list 
# return merged list but it ALSO must be sorted across ALL nodes

# APPROACH
# one pointer for each list
# can do an extra result list but to save space can just reorient the existing list pointers
# smaller value always repointed to larger value
# the repointed value gets incremented
# then compared at the location of both pointers again
# this way the subsequent of the same list will be compared against the newly pointed node
# if lists are of different lenghts
# whatever is remaining is sorted so the pointer can just point at the head of the leftovers
# the rest will fall in line

# time: should be O(n) only see each node once
# space: O(1) only pointer and scratch var no extra list bc we remap

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = tail = ListNode() #empty

        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
            
        tail.next = list1 or list2 #leftovers already sorted
        tail = tail.next
        head = head.next # bc init as null

        return head
            









        