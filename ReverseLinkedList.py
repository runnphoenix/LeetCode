# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
		if head == None:
			return head
		elif head.next == None:
			return head
	
		secondNode = head.next
		
		if secondNode.next == None:
			head.next = None
			secondNode.next = head
			head = secondNode
		else:
			tail = secondNode
			while tail.next.next:
				head.next = tail.next
				tail.next = tail.next.next
				head.next.next = secondNode
				secondNode = head.next
			
			head.next = tail.next
			head.next.next = secondNode
			
			tail.next = head
			head = head.next
			tail.next.next = None
		
		return head