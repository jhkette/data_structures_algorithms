class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    

    def push(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode;
            self.tail = newNode;
        else:
            self.tail.next = newNode; 
            newNode.prev = self.tail
            self.tail = newNode
        
        self.length += 1
        return self

    def print(self):
        current = self.head
        while current is not None:
            if current.value is not None:
                print(current.value)
            current = current.next


x = DoublyLinkedList()
x.push(2)
x.push(3)
x.print()
