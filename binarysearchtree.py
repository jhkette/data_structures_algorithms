
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
                    current.left = new_node
                    return self
                
                current = current.left
            else:
                if current.right == None:
                    current.right = new_node
                    return self  
                current = current.right

    def bfs(self): 
        node = self.root
        data = [] 
        queue = []; 
        queue.append(node); 

        while len(queue) > 0:
           node = queue.pop(0)
           data.append(node.value)
           if node.left:
                queue.append(node.left)
           if node.right:
               queue.append(node.right)
        
        return data

    def dfs_preorder(self):
        data = []
        def traverse(node):
            data.append(node.value)
            if node.left: 
                traverse(node.left)
            if node.right: 
                traverse(node.right)    
        traverse(self.root)
        return data

    def dfs_postorder(self):
        data = []
        def traverse(node):
            if node.left: 
                traverse(node.left)
            if node.right: 
                traverse(node.right)
            data.append(node.value)
        traverse(self.root)
        return data


    def dfs_inorder(self):
        data = []
        def traverse(node):
            if node.left: 
                traverse(node.left)
            data.append(node.value)
            if node.right: 
                traverse(node.right)
        traverse(self.root)
        return data
    

x = Binary_search_tree()

x.insert(2)
x.insert(3)
x.insert(12)
x.insert(5)

y = x.bfs()
z = x.dfs_inorder()
a = x.dfs_postorder()
b = x.dfs_postorder()
print(y)
print(z)
print(a)
print(b)
        
    

