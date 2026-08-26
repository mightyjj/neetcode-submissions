class Node:
    def __init__(self, val: int):
        self.value = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next
        if curr:
            return curr.value
        else:
            return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        
    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def remove(self, index: int) -> bool:
        if self.head is None or index < 0:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        for i in range(index - 1):
            if curr.next is None:
                return False
            curr = curr.next
        if curr.next is None:
            return False
        curr.next = curr.next.next
        return True
    
    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
    