# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lst=list()
        while(head):
            x=head.val
            if x in lst:
                return True
            lst.append(x)
            head=head.next
        return False        
        