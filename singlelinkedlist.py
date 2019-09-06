# simple single linked list in

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        current = self.head
        if not self.head:
            self.head = newNode;
            self.tail = self.head;
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.length += 1
        return self

       
    def pop(self):
        if not self.head:
            return None
        current = self.head
        newTail = current
        while current.next is not None:
            newTail = current
            current = current.next
        self.tail  = newTail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return self.length

    def shift(self):
        if not self.head:
            return None
        current = self.head
        self.head = current.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current

    def unshift(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode   
        else:
            newNode.next = self.head
            self.head = newNode
        
        self.length += 1
        return self

    def get(self, index):
        if(index < 0 or index >= self.length): 
            return None
        counter = 0
        current = self.head
        while(counter != index):
            current = current.next
            counter +=1 
        return current

    def set(self, index, val):
        foundIndex = self.get(index)
        if foundIndex:
            foundIndex.value = val
            return True
        
        return False
    
    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False
    


    def delete(self, value):
        if self.find(value) is not True:
            return 'Not in list'
        else:
            current = self.head
            while current is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                else:
                    current = current.next

    def print(self):
        current = self.head
        while current is not None:
            if current.value is not None:
                print(current.value)
            current = current.next
    

v = List(None)

v.push(10)
v.push(20)
v.push(30)
v.print()
print('---')
x = v.pop()
print(x)
# v.print()
v.push(30)
v.print()
v.shift()
print('---')
v.unshift(9)
v.print()
v.set(2, 'this works')
y = v.get(2)
print(y.value)
print('hi')