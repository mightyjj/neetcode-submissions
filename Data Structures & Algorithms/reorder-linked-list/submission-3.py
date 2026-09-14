# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        1) split the arr in half
        2) reverse second half
        3) merge the now two new heads of linked lists
        """

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ptr = slow.next
        slow.next = None
        prev = slow.next

        while ptr:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        
        # now prev is the new head
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        return