class Graph:
    def __init__(self) -> None:
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []  

    def addEdge(self, v1, v2):
         self.adjacencyList[v1].append(v2)
         self.adjacencyList[v2].append(v1)

    def removeEdge(self, v1,v2):
        self.adjacencyList[v1].remove(v2)
        self.adjacencyList[v2].remove(v1)

    def removeVertex(self, verTex):
        while len(self.adjacencyList.pop(verTex)):
            adjVertex = self.adjacencyList[verTex].pop()
            self.removeEdge(verTex,  adjVertex )

    def depthFirstRecursive(self,start):
        result = []; #  results array
        visited = {}; # visited hash table

        adjList = self.adjacencyList # get the adjacencylist
        
        def dfs(vertex): # function that gets recursively called
            if not vertex: # if the vertex is falsey
                return None
            visited[vertex] = True # the vertex has now been visited
            result.append(vertex) # append the vertex to results
            # this for loop loops through the neighbour vertexes
            for neighbor in adjList[vertex]:
                if neighbor not in visited: #IF the neightbout has not been visited
                    return dfs(neighbor) # return the call of the dfs function with the neighbour
        dfs(start)
        return result
    
    def depthFirstIterative(self,start):
        stack =  [start]
        result = []
        visited = {}
        visited[start] = True
        # currentVertex 
        while(len(stack)): # while the stack has length
            currentVertex = stack.pop() # get the currentVertex
            result.append(currentVertex) # append to result
            for neighbour in self.adjacencyList[currentVertex]:
               
                if neighbour not in visited: # if neighbour not in visited
                    visited[neighbour] = True # visited now equals true
                    stack.append(neighbour) # append neighbour to stack for next call
        return result


g = Graph()
g.addVertex("Dallas")
g.addVertex("Tokyo")
g.addVertex("Aspen")
g.addVertex("Los Angeles")
g.addVertex("Hong Kong")
g.addEdge("Dallas", "Tokyo")
g.addEdge("Dallas", "Aspen")
g.addEdge("Hong Kong", "Tokyo")
g.addEdge("Hong Kong", "Dallas")
g.addEdge("Los Angeles", "Hong Kong")
g.addEdge("Los Angeles", "Aspen")
print(g.adjacencyList)

print(g.depthFirstIterative("Dallas"))