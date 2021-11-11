#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        
        
        if not head or not head.next:
            return True
        
        curr=head
        length=0
        while curr:
            
            curr=curr.next
            length+=1
        current=head
        
        prev=None
        
        temp=None
        for i in range(length//2):
            
            
            temp=current.next
            
            current.next=prev
            prev=current
            current=temp
            
        if length%2!=0:
            temp=temp.next
        # print(temp.data,prev.data)   
            
        while temp and prev:
            # print(temp.data,prev.data)   
            
            if temp.data!=prev.data:
                return False
                
            temp=temp.next
            prev=prev.next
                
        return True