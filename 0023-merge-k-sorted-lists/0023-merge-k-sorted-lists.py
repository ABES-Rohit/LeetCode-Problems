# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sort_list(self,l1,l2):
        res = ListNode()
        l3 = res
        while(l1 and l2):
            if(l1.val<=l2.val):
                l3.next=l1
                l1=l1.next
            else:
                l3.next=l2
                l2=l2.next
            l3=l3.next
        while(l1):
            l3.next=l1
            l1=l1.next
            l3=l3.next
        while(l2):
            l3.next=l2
            l2=l2.next
            l3=l3.next

        return res.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(len(lists)<1):
            return 
        while(len(lists)>1):
            x=self.sort_list(lists[0],lists[1])
            lists.remove(lists[0])
            lists.remove(lists[0])
            lists.insert(0,x)
        return lists[0]
        