#initialise node value
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        self.size = 0


# stack is lifo last IN FIRST OUT
class Stack:
    # init stack class with self.first and self last values
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    
    def push(self, val):
        newNode = Node(val) # create a new node
        if not self.first:
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first # add self.first to temp variable
            self.first = newNode # newnode is self.first and temp is self.first.next
            self.first.next = temp
        self.size += 1
        return self.size

    def pop(self):
        if not self.first: # if no self first return none
            return None
        temp = self.first # return first item as we are popping lifo
        if self.first == self.last:
            self.last = None
        self.first = self.first.next # change self first
        return temp.value # return temp.value


stack = Stack()

stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
