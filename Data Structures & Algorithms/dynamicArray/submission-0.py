class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.length = 0


    def get(self, i: int) -> int:
        if i < self.length:
            return self.arr[i]
       

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
       if self.length > 0:
        t = self.arr[self.length - 1] 
        self.length -= 1
        return t



    def resize(self) -> None:
        self.capacity = self.getCapacity() * 2
        newarr = [0] * self.capacity

        for i in range(self.length):
            newarr[i] = self.arr[i]

        self.arr = newarr


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return len(self.arr)
