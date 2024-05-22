# simple single linked list in
# Node class which contains next value and none value
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

# Class list
# it has a tail and a head
# you add to the tail
class List:
    def __init__(self): # initialise the 
        self.head = None 
        self.tail = None
        self.length = 0
    # push node onto the end of the
    # list
    def push(self, value):
        newNode = Node(value) # create new node
        current = self.head # get the head
        if not self.head: #if there isn't a head it will be the head and the tail
            self.head = newNode
            self.tail = self.head
        else: # if there isn't a head add newNode to self.tail.next then to self.tail
            self.tail.next = newNode
            self.tail = newNode
        
        self.length += 1 # add to length
        return self

       
    def pop(self): # pop the tail
        current = self.head # current  == self.head
        newTail = current # tail - is the current then we start a loop
        while(current.next): #while current.next exists
            newTail = current # the newtail is current
            current = current.next # current is current.next

        self.tail = newTail # current self.tail = newtail
        self.tail.next = None # the next is now none
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current # return is the current which is what we've got from looping

    def shift(self): # retutn the head
        if not self.head:  #if no head return None
            return None
        current = self.head # otherwise current is the head
        self.head = current.next
        self.length -= 1
        if self.length == 0: # if no length the tail is now equal to none
            self.tail = None
        return current # return the current which is the head

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
    

v = List()

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


