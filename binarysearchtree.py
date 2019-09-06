
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        current = self.root
        while True:
            if value == current.value: 
                return None
            if value < current.value:
                if current.left == None:
                    current.left = newNode
                    return self
                
                current = current.left
            else:
                if current.right == None:
                    current.right = newNode
                    return self  
                current = current.right

x = Binary_search_tree()

x.insert(2)


        
    

