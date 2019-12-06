
// BASIC BINARY SEARCH ALGORITHM
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
// LEETCODE https://leetcode.com/problems/search-insert-position/
// # Given a sorted array and a target value, return the index 
// # if the target is found. If not, return the index where it would be 
// # if it were inserted in order.

// # You may assume no duplicates in the array

function searchInsert(nums, target){
    var start = 0
    var end = nums.length -1;
    while(start <= end){
        var middle = Math.floor((start+end)/2)
        if(nums[middle] < target){ // target is greater so
            start = middle + 1 // start become middle +1
        }
        else{
            end = middle -1 // target is less 
        }    
    }
    return start // return start - this is going to be index where item is or should be
}
searchInsert([1,3,5,6], 3)

// LEETCODE
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// # Two pointer technique for finding two sum
// # THIS IS THE WAY TO FIND A SUM FROM AN ARRAY -
// # USING A TWO POINTER TECHNIQUE

function findsum(numbers, target){
    i = 0;
    j = numbers.length -1;
    while(i < j){
       let temp = numbers[i] + numbers[j];
       if(temp == target){
           let arr =[i, j]
           return arr;
       }
        else if(temp < target){
           i ++
        }
        else{
            j --
        }
    }
return []
}




function factorial(num){
    if(num ===1) return 1 //base case
    return num * factorial(num -1) // ie 2 * factorial of 1
}

// const factorial = (num) => {
//     if(num ===1) return 1 //base case
//     return num * factorial(num -1) // ie 2 * factorial of 1
// }

// # https://www.geeksforgeeks.org/find-the-missing-number/
// # // get the missing number in an array ie [1,2,3,4,6,7] => 5

function getMissing(array){
    

}

function linearSearch(arr, val){
    for(var i=0; i < arr.length; i++){
        if(arr[i] === val){
            return i;
        }
    }
    return -1;
}


linearSearch([34,56,23,2], 56)



// reverse a string
function reverse(str){
    var x = str.split('').reverse().join('')
    return x
    
}
// shorter reverse
const reverse2 = (str)  =>  {
   return [...str].reverse.join('')   
}