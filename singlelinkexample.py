Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@jhkette 
1
10 3 AtotheY/YoutubeTutorials
 Code  Issues 1  Pull requests 1  Projects 0  Wiki  Security  Insights
YoutubeTutorials/Introductions/linkedListOnlyNodes.py
@AtotheY AtotheY Added insert code.
0d4ba97 on 15 Apr 2018
91 lines (67 sloc)  2.3 KB
    
# Nodes
# 1. Value - anything strings, integers, objects
# 2. The Next Node


class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


def insertNode(head, valuetoInsert):
    currentNode = head
    while currentNode is not None:
        if currentNode.nextNode is None:
            currentNode.nextNode = linkedListNode(valuetoInsert)
            return head
        currentNode = currentNode.nextNode

# Delete node function
def deleteNode(head, valueToDelete):
    currentNode = head
    previousNode = None
    while currentNode is not None:
        if currentNode.value == valueToDelete:
            if previousNode is None:
                newHead = currentNode.nextNode
                currentNode.nextNode = None
                return newHead
            previousNode.nextNode = currentNode.nextNode
            return head
        previousNode = currentNode
        currentNode = currentNode.nextNode
    return head  # Value to delete was not found.


# "3" -> "7" -> "10"

node1 = linkedListNode("3") # "3"
node2 = linkedListNode("7") # "7"
node3 = linkedListNode("10") # "10"

node1.nextNode = node2 # node1 -> node2 , "3" -> "7"
node2.nextNode = node3 # node2 -> node3 , "7" -> "10"

# node1 -> node2 -> node3

head = node1
print "*********************************"
print "Traversing the regular linkedList"
print "*********************************"
# Regular Traversal
currentNode = head
while currentNode is not None:
    print currentNode.value,
    currentNode = currentNode.nextNode
print ''
print "*********************************"



print "deleting the node '7'"
newHead = deleteNode(head, "10")


print "*********************************"
print "traversing the new linkedList with the node 7 removed"
print "*********************************"


currentNode = newHead
while currentNode is not None:
    print currentNode.value,
    currentNode = currentNode.nextNode


print ''
print "*********************************"
print "Inserting the node '99'"
newHead = insertNode(newHead, "99")


print "*********************************"
print "traversing the new linkedList with the node 99 added"
print "*********************************"


currentNode = newHead
while currentNode is not None:
    print currentNode.value,
    currentNode = currentNode.nextNode

