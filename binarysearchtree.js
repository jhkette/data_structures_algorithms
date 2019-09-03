class Node {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor(){
        this.root = null;
    }
    insert(value){
        var newNode = new Node(value); // new node
        if(this.root === null){ // check if there is a root
            this.root = newNode; //asign root if none exists - it equal NEWDODE
            return this; // return to stop method
        }
        var current = this.root; // current == root
        while(true){ // while true // this is always - so we need to make sure we return to break while loop
            if(value === current.value) return undefined; // if value == current value ignore
            if(value < current.value){ // if value is less - assign to left (if current.left is null)
                if(current.left === null){
                    current.left = newNode;
                    return this;
                }
                current = current.left; //else asign current.left as current - loop starts again
            } else { // the same for right
                if(current.right === null){
                    current.right = newNode;
                    return this;
                } 
                current = current.right;
            }
        }
    }
    find(value){
        if(this.root === null) {return false}
        var current = this.root,
        found = false;
        while(current && !found){
            if (value < current.value){
                current = current.left;

            }
            else if(value > current.value){
                current = current.right;
            }
            else{
                found =true
            }

        }
        if(!found) return null;
        return current;

    }
    BFS(){ // uses queue array
        // space complexity - has to store data - so space complexity increases
        var node = this.root, // root
            data = [], // data variable
            queue = []; //queue variable
        queue.push(node); // push node into queue

        while(queue.length){ //start while loop
           node = queue.shift(); //  get first item (FIFO)
           data.push(node.value); //push in value
           if(node.left) queue.push(node.left); //push in nodeleft and noderight
           if(node.right) queue.push(node.right);
        }
        return data;
    }

    DFSpreOrder(){ // KEEPS tree structure
        var data = [];
        function traverse(node){
            data.push(node.value);
            //recursive function call function check if there is a node on left
            // then add value to data. if no more nodes on the left 
            // checks nodes on right
            if(node.left) traverse(node.left); 
            if(node.right) traverse(node.right);
        }
        traverse(this.root) // call traverse 
        return data;
    }

    DFSPostOrder(){
        var data = [];
        function traverse(node){
            if(node.left) traverse(node.left);
            if(node.right) traverse(node.right);
            data.push(node.value);
        }
        traverse(this.root);
        return data;
    }
    DFSInOrder(){ // this returns data in order
        var data = [];
        function traverse(node){
            if(node.left) traverse(node.left);
            data.push(node.value);
            if(node.right) traverse(node.right);
        }
        traverse(this.root);
        return data;
    }

    
}


//      10
//   5     13
// 2  7  11  16

var tree = new BinarySearchTree();
tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(16)
tree.insert(7)
tree.find(9)
tree.find(10)
tree.DFSPostOrder()
tree.DFSpreOrder()
tree.DFSInOrder()

