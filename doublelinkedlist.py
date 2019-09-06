

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

    def pop(self):
        if not self.head:
            return None
        poppedNode = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = poppedNode.prev 
            self.tail.next = None
            poppedNode.prev = None
        self.length -= 1
        return poppedNode

    def shift(self):

        if not self.head:
            return None
        old_head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.head = old_head.next
            old_head.next = None
            old_head.prev = None
        return old_head


    
        


    def print(self):
        current = self.head
        while current is not None:
            if current.value is not None:
                print(current.value)
            current = current.next


x = DoublyLinkedList()
x.push(2)
x.push(3)
x.push(5)
x.print()
x.pop()
x.shift()
print('-----')
x.print()
