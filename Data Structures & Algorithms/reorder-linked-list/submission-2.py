# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        newHalf = slow.next
        slow.next = None
        prev = None

        while newHalf:
            temp = newHalf.next
            newHalf.next = prev
            prev = newHalf
            newHalf = temp
        
        # now merge it
        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            second = temp2
            first = temp1
        

            