# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, root: Optional[ListNode]) -> Optional[ListNode]:
        
        if not root:
            return root
        
        if not root.next:
            return None
        
        slow=fast=root
        prev=None
        
        
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
            
            
        prev.next=slow.next
        
        return root
            
            
        
        