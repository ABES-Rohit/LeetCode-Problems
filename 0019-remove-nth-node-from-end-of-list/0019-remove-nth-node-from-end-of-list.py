# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy1=head
        dummy2=head
        s=0
        while(dummy1!=None):
            s=s+1
            dummy1=dummy1.next
        k=s-n
        if(k==0):
            return head.next
        c=-1
        while(dummy2!=None):
            c=c+1
            if((c+1)==k):
                dummy2.next=dummy2.next.next
            dummy2=dummy2.next
        return head                