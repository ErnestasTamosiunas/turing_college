class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        output = ""
        for _ in range(self.size):
            output += "🍪"
        return output

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if self.size - n >= 0:
            self.size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
