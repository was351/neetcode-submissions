class MinStack:

    def __init__(self):
        self.my_arr = []
        self.arr_min = float('inf')

    def push(self, val: int) -> None:
        self.my_arr.append(val)
        if val < self.arr_min:
            self.arr_min = val

    def pop(self) -> None:
        temp = self.my_arr.pop()
        if not self.my_arr:
            self.arr_min = float('inf')
        elif temp == self.arr_min:
            self.arr_min = min(self.my_arr)

    def top(self) -> int:
        return self.my_arr[-1]

    def getMin(self) -> int:
        return self.arr_min

