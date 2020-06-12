class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        self.oldest = 0

    def append(self, item):
        if len(self.data) >= self.capacity:
            self.data.pop(self.oldest)
            self.data.insert(self.oldest, item)
            self.oldest += 1
        if len(self.data) < self.capacity:
            self.data.append(item)
        if self.oldest >= self.capacity:
            self.oldest = 0

    def get(self):
        return self.data 