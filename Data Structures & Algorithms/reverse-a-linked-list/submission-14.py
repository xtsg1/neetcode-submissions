# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# first attempt Nov 9

# Approach
# starting at head of linked list
# keep checking if next points to null
# if null then thats the tail
# how to reverse it?
# tail becomes new head
# store into a list
# reverso the list?
# thats it??

# time: O(n) once through the whole linked list, then reversal
# space: O(n) store a whole new list

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head

        while cur:
            follow = cur.next
            cur.next = prev
            prev = cur
            cur = follow
        
        return prev
        

            





        