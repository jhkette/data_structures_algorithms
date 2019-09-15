class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val){
        var newNode = new Node(val)
        if(!this.head){ //if the list is empty
            this.head = newNode;
            this.tail = this.head;
        } else{
            this.tail.next = newNode; // add new node
            this.tail = newNode; // make it the tail
        }
        this.length++;
        return this;
    }
    pop(){
        if(!this.head){
            return null
        }
        var current = this.head;
        var newTail = current;
        while(current.next){ 
            newTail = current;
            current = current.next;
        }
        this.tail  = newTail;
        this.tail.next = null;
        this.length --;
        if(this.length === 0){ // edge case if no items left - remove head and tail
            this.head = null;
            this.tail = null;
        }
        return current;
    }
    shift(){
        if(!this.head){
            return null
        }
        var current = this.head;
        this.head = current.next;
        this.length --;
        if(this.length === 0){ // edge case if no items left - remove head and tail
            this.tail = null;
        }
        return current;
    }
    unshift(val){
        var newNode = new Node(val)
        if(!this.head){
            this.head = newNode
            this.tail = newNode
        }
        else{
        newNode.next = this.head;
        this.head = newNode;
        }
        this.length++;
        return this;

    }
    get(index){
        if(index < 0 || index >= this.length) return null;
        var counter = 0;
        var current = this.head;
        while(counter !== index){
            current = current.next;
            counter++;
        }
        return current;
    }
    set(index, val){
        var foundIndex = this.get(index);
        if(foundIndex){
            foundIndex.val = val;
            return true
        }
        return false;
    }
    delete(index){
        if(index < 0 || index >= this.length) return null;

    }
}

var list = new SinglyLinkedList()

list.push("HELLO")  
list.push("GOODBYE") 
list.push("!") 
list.push("<3")
list.push(":)") 