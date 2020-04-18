# Implement a queue by using two stacks


class Queue(object):
    def __init__(self):
        self._s1 = []
        self._s2 = []

    def enqueue(self, item):
        self._s1.append(item)

    def dequeue(self):
        if self._s2:
            return self._s2.pop()
        else:
            while self._s1:
                self._s2.append(self._s1.pop())
            return self._s2.pop()

# T:O(1) S:O(n)

# Test
test_queue = Queue()
test_queue.enqueue(1)
test_queue.enqueue(2)
test_queue.enqueue(3)
print(test_queue.dequeue())
print(test_queue.dequeue())
