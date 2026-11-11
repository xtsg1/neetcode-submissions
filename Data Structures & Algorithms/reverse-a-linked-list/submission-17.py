# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 2nd attempt nov 11

# APPROACH
# so basically traverse the list until i find the tail
# that tail becomes the new head of the list
# at each step of the way switch the connection to be the opposite way
# lot of symbol shunting
# 2 pointers
# temp var to store next pointer when swapping

# WALKTHROUGH

# None > 0  >  1  >  2  >  3 > None
# None < 0  <  1  <  2  <  3 > None
#                               j                
#                          i
#                               k

# FINISHED: 9:52

class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        i = None
        j = head
        while j != None:
            k = j.next  # temp subsequent node
            j.next = i
            i = j
            j = k
        
        newHead = i
        return newHead




        