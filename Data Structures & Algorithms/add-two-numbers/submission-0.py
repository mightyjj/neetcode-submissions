# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstPlace, secondPlace = 0, 0
        firstNum, secondNum = 0, 0
        while l1:
            firstNum += l1.val * (10 ** firstPlace)
            firstPlace += 1
            l1 = l1.next

        while l2:
            secondNum += l2.val * (10 ** secondPlace)
            secondPlace += 1
            l2 = l2.next
        
        dummy = ListNode(0)
        finalNum = firstNum + secondNum
        prev = dummy

        for num in str(finalNum)[::-1]:
            temp = ListNode(int(num))
            prev.next = temp
            prev = temp

        return dummy.next