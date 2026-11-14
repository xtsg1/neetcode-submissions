# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# QUESTION
# merge the two lists
# not necessarily same number of nodes
# both are sorted tho
# returned list must be sorted

# APPROACH
# head pointer at lowest first node
# compare same node from both lists
# tail will always point to lower of the 2
# increment only the node that was just pointed to must be done in same operation
# this way the comparison will always work
# at the end if any list has extra elements append them in order (since they'll already be sorted)

# Time: O(n) every element once
# Space: O(n) will use a separate linked list to store merged

# WALKTHROUGH

#     h 
#     1 - 1   2   4   None
#         | / | / |
#         1   3   5 - 8 9 9 9

 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        tail = head

        if not list1:  #edge case
            return list2
        if not list2:
            return list1 

        while list1 and list2: 
            
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        tail.next = list1 or list2 # leftover lists
        head = head.next # move up head 1
        return head
        


        




