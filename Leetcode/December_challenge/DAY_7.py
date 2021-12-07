# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        string=""
        
        while head:
            string+=str(head.val)
            head=head.next
            
        # print(string)
            
            
        ans=0
        count=0
        for i in string[::-1]:
            
            if i=="1":
                ans+=pow(2,count)
            count+=1
                
        return ans