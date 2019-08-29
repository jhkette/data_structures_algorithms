
function factorial(num){
    if(num ===1) return 1 //base case
    return num * factorial(num -1) // ie 2 * factorial of 1
}

// const factorial = (num) => {
//     if(num ===1) return 1 //base case
//     return num * factorial(num -1) // ie 2 * factorial of 1
// }

function linearSearch(arr, val){
    for(var i=0; i < arr.length; i++){
        if(arr[i] === val){
            return i;
        }
    }
    return -1;
}


linearSearch([34,56,23,2], 56)



function binarySearch(arr,elem){
    var start =0; // start
    var end = arr.length -1; // end
    var middle = Math.floor((start + end)/2) // middle
    while(arr[middle] !== elem && start <= end){  //while middle does not == elem and start does not == end
        if(elem <arr[middle]){ // if middle is < than elem -> end -1
            end = middle -1; // middle -1
        } else{ //else start +1
            start = middle + 1;
        }
        middle = Math.floor((start + end)/2) // re find math.floor()
    }
    if(arr[middle] === elem){
        return middle
    }
    return -1;
}

// refactored version of binary search
function search (arr,target){
    var start = 0;
    var end = arr.length -1;
    while(start <= end){
        var middle = Math.floor((start+end)/2)
        if(arr[middle]==target){
            return middle;
        }
        else{
            if(target < arr[middle]){
                end = middle -1
            }
            else{
                start = middle +1
            }
        }
    
    }
    return -1;
}