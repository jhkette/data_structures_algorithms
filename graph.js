class Graph {
    constructor(){
        this.adjacencyList = {}
    }

    addVertex(vertex){
        if(!this.adjacencyList[vertex])  this.adjacencyList[vertex] = []
    }
    addEdge(vertex1, vertex2){
        if(this.adjacencyList[vertex1]) this.adjacencyList[vertex1].push(vertex2)
        if(this.adjacencyList[vertex2]) this.adjacencyList[vertex2].push(vertex1)

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


