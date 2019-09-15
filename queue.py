

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

# queue is fifo FIRST IN FIRST OUT

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        