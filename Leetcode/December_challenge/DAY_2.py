class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        odd = head
        even = head.next
        
        x = even.next 
        
        while x:
            temp = x
            even.next = x.next
            even = even.next
			
            temp.next = odd.next
            odd.next = temp
            odd = odd.next
			
            x= even.next if even else None
            
        return head
            