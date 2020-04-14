# How can you implement a queue with two stacks?

class Solution(object):
    def __init__(self):
        if not input:
            return
        self.s1 = []
        self.s2 = []

    def enQueue(self, value):
        self.s1.append(value)

    def deQueue(self):
        if self.s2:
            self.s2.pop()
        # If s2 is empty, move all s1 elements to s2
        else:
            while self.s1:
                self.s2.append(self.s1.pop())

# T:O(1) S:O(n)
