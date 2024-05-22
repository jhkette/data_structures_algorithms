class Graph {
    constructor(){
        this.adjacencyList = {}
    }

    addVertex(vertex){
        if(!this.adjacencyList[vertex]){  
            this.adjacencyList[vertex] = []
        }
    }
    addEdge(vertex1, vertex2){
        if(this.adjacencyList[vertex1]){ 
            this.adjacencyList[vertex1].push(vertex2)
        }
        if(this.adjacencyList[vertex2]) {
            this.adjacencyList[vertex2].push(vertex1)
        }

    }
    removeEdge(v1,v2){
        this.adjacencyList[v1].filter((vs) => {
            return vs !== v2
        })
        this.adjacencyList[v2].filter((vs) => {
            return vs !== v1
        })  
    }
    removeVertex(vertex){
        while(this.adjacencyList[vertex].length){
            const adjacentVertex = this.adjacencyList[vertex].pop();
            this.removeEdge(vertex, adjacentVertex);
        }
        delete this.adjacencyList[vertex]
    }
    depthFirstRecursive(start){
        const result = []; // results array
        const visited = {}; // visited hash table
        const adjacencyList = this.adjacencyList; // asign this.adjancency list 
        //to variable here

        (function dfs(vertex){ // recursive function iife
            if(!vertex) return null; // if no vertex return null
            visited[vertex] = true; // add that the vertex is visited 'true' to hash table
            result.push(vertex); // push result to array
            adjacencyList[vertex].forEach((neighbor) => { //loop through the vertex array
                if(!visited[neighbor]){
                    return dfs(neighbor) // and call dfs again
                }
            });
        })(start); // start dfs function with initial argument

        return result;
    }

    depthFirstIterative(start){
        const stack =  [start]; // add start to stacl
        const result = []; // results array
        const visited = {}; // visited hash table
        visited[start] = true; // set it's value to true
        let currentVertex // current vertex
        while(stack.length){ // while stack.length
            currentVertex = stack.pop() // pop the last stack item
            result.push(currentVertex); // push in vertex

            this.adjacencyList[currentVertex].forEach((neighbour)=>{ // for each neighbour
                if(!visited[neighbour]){
                    visited[neighbour] = true; // add true to hash table
                    stack.push(neighbour) // push to stack
                }
            })
        }
        return result

    }

    breadthFirst(start){
        const queue = [start];
        const result = [];
        const visited = {};
        let currentVertex;
        visited[start] = true;

        while(queue.length){
            currentVertex = queue.shift();
            result.push(currentVertex);
           

            this.adjacencyList[currentVertex].forEach(neighbor => {
                if(!visited[neighbor]){
                    visited[neighbor] = true;
                    queue.push(neighbor);
                }
            });
        }
        return result;
    }
}

let g = new Graph();
g.addVertex("Dallas");
g.addVertex("Tokyo");
g.addVertex("Aspen");
g.addVertex("Los Angeles");
g.addVertex("Hong Kong")
g.addEdge("Dallas", "Tokyo");
g.addEdge("Dallas", "Aspen");
g.addEdge("Hong Kong", "Tokyo");
g.addEdge("Hong Kong", "Dallas");
g.addEdge("Los Angeles", "Hong Kong");
g.addEdge("Los Angeles", "Aspen");
console.log(g.depthFirstIterative("Dallas"))
console.log(g.adjacencyList)

