# initialise node class
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

# queue is fifo FIRST IN FIRST OUT

# queue class
class Queue:
    def __init__(self): # initialise self.first and last values of queue
        self.first = None 
        self.last = None
        self.size = 0
    # enqueue add new node to self.last.next if there are nodes
    # create self.first and self.last if there are no nodes
    def enqueue(self,val): 
        newNode = Node(val)
        if newNode.first == None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
        self.size += 1
        return self.size

    def dequeue(self,val): # dequeue returns the first node in
        if self.first == None:

            return None
        
        temp = self.first # so the first is temp self.first
        if self.first == self.last:
            self.last = None
        
        self.first = self.first.next # selffirst is sefftirst.next
        self.size -= 1
        return temp.value # we return temp.value


        
