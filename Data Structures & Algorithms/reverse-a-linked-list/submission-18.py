# GREEN 2026-11-11 | cold, first try, 9:52 | complexity: O(n) time, O(1) space
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

# each element accessed once so time: O(n)
# only scratch variables are pointers so: O(1) space

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




        