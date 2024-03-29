class Node{
    constructor(val){
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
    push(val){
        var newNode = new Node(val)
        if(!this.head){ //if the list is empty
            this.head = newNode;
            this.tail = newNode;
        } else{
            this.tail.next = newNode; // add new node
            newNode.prev = this.tail
            this.tail = newNode; // make it the tail
        }
        this.length++;
        return this;
    }
    pop(){
        if(!this.head){
            return null
        }
       var  poppedNode = this.tail;
       if(this.length == 1){
           this.head = null;
           this.tail = null;
       }else{
          this.tail = poppedNode.prev 
          this.tail.next = null;
          poppedNode.prev = null;
       }
       
       this.length --;
       return poppedNode;
    }
    shift(){
        if(this.length === 0) return undefined;
        var oldHead = this.head;
        if(this.length === 1){
            this.head = null;
            this.tail = null;
        }else{
            this.head = oldHead.next;
            this.head.prev = null;
            oldHead.next = null;
        }
        this.length--;
        return oldHead;
    }
}