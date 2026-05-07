class MinStack:

    def __init__(self):
        self._my_array = []

    def push(self, val: int) -> None:
        if not self._my_array:
            self._my_array.append((val, val))
        else:
            current_min = min(val, self._my_array[-1][1])
            self._my_array.append((val, current_min))

    def pop(self) -> None:
        self._my_array.pop()

    def top(self) -> int:
        return self._my_array[-1][0]

    def getMin(self) -> int:
        return self._my_array[-1][1]
