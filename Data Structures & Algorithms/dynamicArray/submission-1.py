class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.curr_holds = 0

    def get(self, i: int) -> int:
        if 0 <= i < self.curr_holds:
            return self.arr[i]
        return None

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.curr_holds:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.curr_holds == len(self.arr):
            self.resize()
        self.arr[self.curr_holds] = n
        self.curr_holds += 1

    def popback(self) -> int:
        res = self.arr[self.curr_holds - 1]
        self.arr[self.curr_holds - 1] = None
        self.curr_holds -= 1
        return res

    def resize(self) -> None:
        self.arr.extend([None] * len(self.arr))

    def getSize(self) -> int:
        return self.curr_holds
    
    def getCapacity(self) -> int:
        return len(self.arr)