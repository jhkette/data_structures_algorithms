
// the pivot function returns the correct index of the pivot in a
// sorted list
function pivot(arr, start = 0, end = arr.length - 1) {
  // basic swap function - we literally just swap the array values
  const swap = (arr, idx1, idx2) => {
    [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
  };

  // We are assuming the pivot is always the first element
  let pivot = arr[start];
  let swapIdx = start; // this is going to start as 0 but will be added to.

  for (let i = start + 1; i <= end; i++) {
    if (pivot > arr[i]) { //if greater check
      swapIdx++; // if greater add to swapidx as there is one greater
      swap(arr, swapIdx, i); // call swap to swap the number that is grater than pivot
    }
  }

  // Swap the pivot from the start the swapPoint
  swap(arr, start, swapIdx); // this is the final swap that moves the initial pivot to it's correct position
  return swapIdx;
}
/**
 *- call the pivot helper on the array
 * - when the helper returns the updated pivot index recursively
 * - call the pivot helper on the subarray to the left of that index
 * - the base case is when you consider an array with less than two elements
 *  - or in the code if left value is greater than right
 * @param Array arr 
 * @param int left 
 * @param int right 
 * @returns 
 */

function quickSort(arr, left = 0, right = arr.length -1){ // 
    if(left < right){
        let pivotIndex = pivot(arr, left, right) // call pivot index 
        // Recursive call on the left of pivot
        quickSort(arr,left,pivotIndex-1); // recursively call quickosrt
        // Recursive call on the right of pivot
        quickSort(arr,pivotIndex+1,right); // recursively call quickosrt
      }
     return arr;
} 
           
quickSort([100,-3,2,4,6,9,1,2,5,3,23])




// [4,6,9,1,2,5,3]
// [3,2,1,4,6,9,5]
//        4
//  3,2,1    6,9,5
//      3      6
//  2,1      5  9
//    2
//  1




