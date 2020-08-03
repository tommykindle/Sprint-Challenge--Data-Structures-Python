class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.index += 1
        elif self.index >= self.capacity:
            self.storage[0] = item
            self.index = 1
        else:
            self.storage[self.index] = item
            self.index += 1

    def get(self):
        return self.storage
